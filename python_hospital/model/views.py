from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Visu

def index(request):
    template = loader.get_template('model/index.html')
    contexte = {}
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
    return HttpResponse("Menu avec toutes les visus ")


def visu(request, visu_id):
    response = "You're looking at visu %s"
    return HttpResponse(response % visu_id)

def model(request, model_id):
    response = "You're looking at model %s"
    return HttpResponse(response % model_id)