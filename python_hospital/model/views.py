import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Visu

#les views
def index(request):
    template = loader.get_template('model/index.html')

    df = read_data()
    data = [len(df[df.diabetesMed == "Yes"]), len(df[df.diabetesMed == "No"])]
    contexte = {'data': data}
    return HttpResponse(template.render(contexte, request));

def welcome(request):
    template = loader.get_template('model/welcome.html')
    context = {}
    return HttpResponse(template.render(context,request))

def who(request):
    template = loader.get_template('model/who.html')
    context = {}
    return HttpResponse(template.render(context,request))

def context(request):
    template = loader.get_template('model/context.html')
    context = {}
    return HttpResponse(template.render(context,request))

def dataviz(request):
    template = loader.get_template('model/dataviz.html')
    list_visu_info = Visu.objects.filter(visu_zone = "INFO")
    list_visu_comprendre = Visu.objects.filter(visu_zone = "COMPRENDRE")
    list_visu_impact = Visu.objects.filter(visu_zone = "IMPACT")
    context = {'list_info': list_visu_info, 'list_comprendre':list_visu_comprendre, 'list_impact' : list_visu_impact}
    return HttpResponse(template.render(context,request))


def visu(request, visu_id):
    template = loader.get_template('model/visu.html')
    visu = Visu.objects.get(pk=visu_id)

    df = read_data()

    label_choice = visu.visu_label
    labels = df[label_choice].unique()

    values = visu.visu_values
    data = []

    if(values == "COUNT"):
        for index in labels:
            data.append(len(df[df[label_choice] == index]))



    contexte = {'data': data, 'labels':labels, 'visu':visu}

    return HttpResponse(template.render(contexte, request));

def model(request, model_id):
    response = "You're looking at model %s"
    return HttpResponse(response % model_id)




#preprocessing
def read_data():
    d = os.getcwd() #chemin du projet
    data_path = d+'/model/static/data/diabetic_data.csv'

    mapping_path = "/static/data/IDs_mapping.csv"

    df = pd.read_csv(data_path, header ="infer")

    df = df.drop(df[df["discharge_disposition_id"] == 11 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 13 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 14 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 19 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 20 ].index)
    df = df.drop(df[df["discharge_disposition_id"] == 21 ].index)
    #11,Expired
    #13,Hospice / home
    #14,Hospice / medical facility
    #19,"Expired at home. Medicaid only, hospice."
    #20,"Expired in a medical facility. Medicaid only, hospice."
    #21,"Expired, place unknown. Medicaid only, hospice."

    df.drop(['race','encounter_id','patient_nbr'],axis=1,inplace=True)

    url="https://en.wikipedia.org/wiki/List_of_ICD-9_codes_001%E2%80%93139:_infectious_and_parasitic_diseases"
    page=requests.get(url)
    html_soup=BeautifulSoup(page.content,'html.parser')
    table = html_soup.find_all('table',{"class":"wikitable"})
    df_list = pd.read_html(str(table),header=None)[0]
    df_list.drop(labels="Chapter",inplace=True,axis=1)

    return df

#preparation visus 
