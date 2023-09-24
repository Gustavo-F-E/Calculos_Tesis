from django.shortcuts import render

from django.http import HttpResponse 
from django.template import loader 

# Create your views here. 

 

def index(request): 
    template = loader.get_template('calculos_tesis_app/index.html') 
    return HttpResponse(template.render()) 


def regla_mezclas_teoria(request): 
    template = loader.get_template('calculos_tesis_app/regla_mezclas_teoria.html') 
    return HttpResponse(template.render()) 

def regla_mezclas_calculos(request): 
    template = loader.get_template('calculos_tesis_app/regla_mezclas_calculos.html') 
    return HttpResponse(template.render()) 

def modelo_microestructura_periodica_teoria(request): 
    template = loader.get_template('calculos_tesis_app/modelo_microestructura_periodica_teoria.html') 
    return HttpResponse(template.render()) 

def modelo_microestructura_periodica_calculos(request): 
    template = loader.get_template('calculos_tesis_app/modelo_microestructura_periodica_calculos.html') 
    return HttpResponse(template.render()) 