# -*- encoding: utf-8 -*-
from django import forms
from django.forms.models import ModelForm

from proyectos.models import Proyecto


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'slogan', 'desc','info','repo','web','docu','tipo','techs']
        widgets={
                      "titulo":forms.TextInput(attrs={'placeholder':'Titulo','class':'form-control'}),
                      "slogan":forms.TextInput(attrs={'placeholder':'Slogan', 'class':'form-control'}),
                      "desc":forms.Textarea(attrs={'placeholder':'Máximo 150 caracteres', 'class':'form-control', 'rows':3}),
                      "info":forms.Textarea(attrs={'placeholder':'Máximo 500 caracteres', 'class':'form-control'}),
                      "repo":forms.TextInput(attrs={'placeholder':'Http://...', 'class':'form-control'}),
                      "web":forms.TextInput(attrs={'placeholder':'Http://...', 'class':'form-control'}),
                      "docu":forms.TextInput(attrs={'placeholder':'Http://...', 'class':'form-control'}),
                      "tipo":forms.Select(attrs={'placeholder':'Tipo', 'class':'form-control'}),
                      "techs":forms.SelectMultiple(attrs={'placeholder':'Tecnologías', 'class':'form-control'}),
                  }  
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)

        self.fields['docu'].label = "Documentación"
        self.fields['desc'].label = "Descripción"
        self.fields['techs'].label = "Tecnologías"


            
