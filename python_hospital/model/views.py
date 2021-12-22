import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests 
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import xgboost as xgb


from scipy.stats import uniform, randint

from sklearn.datasets import load_breast_cancer, load_diabetes, load_wine
from sklearn.metrics import auc, accuracy_score, confusion_matrix, mean_squared_error
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold, RandomizedSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pickle

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Visu, Pred

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

    values_choice = visu.visu_values
    data = []
    values = []

    if(values_choice == "COUNT"):
        for index in labels:
            data.append(len(df[df[label_choice] == index]))

    else:
        values = df[values_choice].unique()
        for value in values : 
            temp = []
            df1 = df[df[values_choice]== value]
            for index in labels:
                temp.append(len(df1[df1[label_choice]==index]))
            data.append(temp)
    


    contexte = {'data': data, 'labels':labels, 'visu':visu}
    if(values_choice != "COUNT"):
        contexte["choice"] = True
        contexte["values"] = values
    

    return HttpResponse(template.render(contexte, request));

def models(request):
    template = loader.get_template('model/models.html')
    list_pred = Pred.objects.all()
    context = {'list_preds': list_pred }
    return HttpResponse(template.render(context,request))

def pred(request, pred_id):
    template = loader.get_template('model/pred.html')
    pred = Pred.objects.get(pk=pred_id)

    #Convert your prediction object into a tab 

    #toutes les valeurs numeriques
    temp_integer = []
    temp_integer.append(pred.time_in_hospital)
    temp_integer.append(pred.num_lab_procedures)
    temp_integer.append(pred.num_procedures)
    temp_integer.append(pred.num_medications)
    temp_integer.append(pred.number_outpatient)
    temp_integer.append(pred.number_emergency)
    temp_integer.append(pred.number_inpatient)
    temp_integer.append(pred.number_diagnoses)

    temp_gender = [0 for i in range(0,3)]
    temp_gender[pred.gender] = 1

    temp_age = [0 for i in range(0,10)]
    temp_age[pred.age]=1

    temp_speciality = [0 for i in range(0,71)]
    temp_speciality[pred.speciality]=1

    temp_diag1 = [0 for i in range(0,19)]
    temp_diag1[pred.diagnostique_1]=1
    temp_diag2 = [0 for i in range(0,19)]
    temp_diag2[pred.diagnostique_2]=1
    temp_diag3 = [0 for i in range(0,19)]
    temp_diag3[pred.diagnostique_3]=1

    temp_glu = [0 for i in range(0,4)]
    temp_glu[pred.max_glue]=1

    temp_ac1 = [0 for i in range(0,4)]
    temp_ac1[pred.AC1result]=1

    temp_med = [0 for i in range(0,66)]
    temp_med[pred.metformin]=1
    temp_med[pred.repaglidine]=1
    temp_med[pred.nateglidine]=1
    temp_med[pred.chlorpropadine]=1
    temp_med[pred.glimepiride]=1
    temp_med[pred.acetohexamide]=1
    temp_med[pred.glizipide]=1
    temp_med[pred.glyburide]=1
    temp_med[pred.tolbutamide]=1
    temp_med[pred.pioglitazone]=1
    temp_med[pred.rosiglitazone]=1
    temp_med[pred.acarbose]=1
    temp_med[pred.miglitol]=1
    temp_med[pred.troglitazone]=1
    temp_med[pred.tolazamide]=1
    temp_med[pred.insulin]=1
    temp_med[pred.glybu_met]=1
    temp_med[pred.glypy_met]=1
    temp_med[pred.glim_pio]=1
    temp_med[pred.met_ros]=1
    temp_med[pred.met_pio]=1


    temp_change = [0 for i in range(0,2)]
    temp_change[pred.change_medication]=1

    temp_med_diabete = [0 for i in range(0,2)]
    temp_med_diabete[pred.diabetes_med]=1

    temp_admissionT = [0 for i in range(0,8)]
    temp_admissionT[pred.admission_type]=1

    temp_discharge = [0 for i in range(0,21)]
    temp_discharge[pred.discharge]=1

    temp_admissionS = [0 for i in range(0,17)]
    temp_admissionS[pred.admission_soucre]=1

    predict = temp_integer + temp_gender + temp_age + temp_speciality + temp_diag1 + temp_diag2 + temp_diag3 + temp_glu + temp_ac1+ temp_med+ temp_change+ temp_med_diabete+ temp_admissionT+ temp_discharge+ temp_admissionS
     
    d = os.getcwd() #chemin du projet
    filename = d+'/model/static/data/finalized_model.sav'
    predicts = pd.DataFrame(predict).transpose()

    loaded_model = pickle.load(open(filename, 'rb'))
    
    class_pred = loaded_model.predict(predicts)
    class_prob= loaded_model.predict_proba(predicts)

    classe = class_pred[0]
    proba_no = round(class_prob[0][0]*100,1)
    proba_yes = round(class_prob[0][1]*100,1)


    contexte = {'pred':pred, 'predict':predict, "class_pred":classe, "proba_no":proba_no, "proba_yes":proba_yes }

    return HttpResponse(template.render(contexte, request));






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
