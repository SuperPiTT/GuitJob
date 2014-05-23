import re

from django.shortcuts import render
from django.views.generic.base import TemplateView


semana   = {0:'Domingo', 
              1:'Lunes', 
              2:'Martes', 
              3:'Miercoles', 
              4:'Jueves',  
              5:'Viernes', 
              6:'Sabado'}

mes   = {1:'Enero', 
              2:'Febrero', 
              3:'Marzo', 
              4:'Abril', 
              5:'Mayo',  
              6:'Junio', 
              7:'Julio',
              8:'Agosto',
              9:'Septiembre',
              10:'Octubre',
              11:'Noviembre',
              12:'Diciembre',}

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)


# Create your views here.
class IndexView(TemplateView):
    template_name = "principal/index.html"