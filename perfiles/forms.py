# -*- encoding: utf-8 -*-
from django import forms
from django.forms import extras
from django.forms.models import ModelForm, inlineformset_factory

from perfiles.models import Perfil, Conocimiento


GENEROS=[('H','Hombre'),
         ('M','Mujer')]


class SignupForm(forms.Form):
    nombre = forms.CharField(max_length=30, label='Nombre', 
                    widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellidos = forms.CharField(max_length=30, label='Apellidos', 
                    widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    cumple = forms.DateField(label='Fecha de Nacimiento', widget=extras.SelectDateWidget(attrs={'class': 'datepicker'}))
    genero = forms.ChoiceField(choices=GENEROS, widget=forms.RadioSelect())
    



    def save(self, user):
        perfil = Perfil(user=user)
        user.first_name = self.cleaned_data['nombre']
        user.last_name = self.cleaned_data['apellidos']
        perfil.nombre = self.cleaned_data['nombre']
        perfil.apellidos = self.cleaned_data['apellidos']
        perfil.cumple = self.cleaned_data['cumple']
        perfil.genero = self.cleaned_data['genero']
        user.save()
        perfil.save()
      
class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        exclude = ['fecha_creacion', 'fecha_modificacion', 'user', 'foto_social']
        widgets={
                      "nombre":forms.TextInput(attrs={'placeholder':'nombre','class':'form-control'}),
                      "apellidos":forms.TextInput(attrs={'placeholder':'apellidos', 'class':'form-control'}),
                      "cumple":forms.DateInput(attrs={'class':'form-control datepicker'}),
                      "geocomplete": forms.TextInput(attrs={'placeholder':'Localización','class':'form-control', 'id':'geocomplete'}),
                      "lat":forms.HiddenInput(),
                      "lng":forms.HiddenInput(),
                      "location":forms.HiddenInput(),
                      "locality":forms.HiddenInput(),
                      "sublocality":forms.HiddenInput(),
                      "country":forms.HiddenInput(),
                      "country_short":forms.HiddenInput(),
                      "administrative_area_level_2":forms.HiddenInput(),
                      "administrative_area_level_1":forms.HiddenInput(),
                      "so": forms.TextInput(attrs={'placeholder':'Sistema operativo','class':'form-control'}),
                      "info": forms.Textarea(attrs={'placeholder':'150 Caracteres','class':'form-control'}),
                      "profesion" : forms.TextInput(attrs={'class':'form-control'}),
                      "conocimiento" : forms.SelectMultiple(attrs={'class':'form-control'}),
                      "google": forms.URLInput(attrs={'placeholder':'google','class':'form-control'}),
                      "facebook": forms.URLInput(attrs={'placeholder':'Facebook','class':'form-control'}),
                      "twitter": forms.URLInput(attrs={'placeholder':'Twitter','class':'form-control'}),
                      "web": forms.URLInput(attrs={'placeholder':'Web','class':'form-control'}),
                  }  

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)

        self.fields['so'].label = "Sistema operativo"
        self.fields['geocomplete'].label = "Localización"
        self.fields['cumple'].label = "Fecha de Nacimiento"
        
class ConocimientoForm(ModelForm):
    class Meta:
        model = Conocimiento
        exclude = ['perfil']
        
ConocimientoFormSet = inlineformset_factory(Perfil, Conocimiento,form=ConocimientoForm, extra=0,max_num=5, validate_max=True, can_delete=True)
