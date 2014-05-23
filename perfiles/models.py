# -*- encoding: utf-8 -*-
from allauth.account.signals import user_signed_up
from django.core.urlresolvers import reverse_lazy, reverse
from django.db import models
from django.dispatch import receiver

from guitjob import settings

NIVELES = (
    ('Aprendiendo', 'Aprendiendo'),
    ('Medio', 'Medio'),
    ('Experto', 'Experto'),
)



class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, related_name="mperfil")
    
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    #id_municipio = models.ForeignKey(Municipios, db_column="id_municipio")
    cumple = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    
    info = models.TextField(max_length=150, blank=True, null=True)
    
    foto = models.ImageField(upload_to="fotos",blank=True, null=True)
    foto_social = models.URLField( blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    lat = models.DecimalField(max_digits=22, decimal_places=18, blank=True, null=True)
    lng = models.DecimalField(max_digits=22, decimal_places=18, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=150, blank=True, null=True)
    sublocality = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    country_short = models.CharField(max_length=5, blank=True, null=True)
    administrative_area_level_2 = models.CharField(max_length=100, blank=True, null=True)
    administrative_area_level_1 = models.CharField(max_length=100, blank=True, null=True)
    geocomplete = models.CharField(max_length=250, blank=True, null=True)
    
    profesion = models.CharField(max_length=50, blank=True, null=True)
    
    google = models.URLField( blank=True, null=True)
    facebook = models.URLField( blank=True, null=True)
    twitter = models.URLField( blank=True, null=True)
    web = models.URLField( blank=True, null=True)
    
    so = models.CharField(max_length=50, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('perfiles_detalle', kwargs={'pk': self.pk})
    def __unicode__(self):
        return '%s %s' % (self.nombre , self.apellidos)

    
# When account is created via social, fire django-allauth signal to populate Django User record.
 
@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    '''
    When a social account is created successfully and this signal is received,
    django-allauth passes in the sociallogin param, giving access to metadata on the remote account, e.g.:
 
    sociallogin.account.provider  # e.g. 'twitter' 
    sociallogin.account.get_avatar_url()
    sociallogin.account.get_profile_url()
    sociallogin.account.extra_data['screen_name']
 
    See the socialaccount_socialaccount table for more in the 'extra_data' field.
    '''

    if sociallogin:
        # Extract first / last names from social nets and store on User record
        if sociallogin.account.provider == 'twitter':
            
            name = sociallogin.account.extra_data['name']
            
            perfil, creado = Perfil.objects.get_or_create(user=user)
            perfil.nombre = name
            #perfil.ciudad = sociallogin.account.extra_data['location']
            
            
            user.first_name = name
 
        if sociallogin.account.provider == 'facebook':
            perfil, creado = Perfil.objects.get_or_create(user=user)
            perfil.nombre = sociallogin.account.extra_data['first_name']
            perfil.apellidos = sociallogin.account.extra_data['last_name']
            #perfil.genero = sociallogin.account.extra_data['gender'] male
            #perfil.idciudad = sociallogin.account.extra_data['hometoen']['id'] 
            #perfil.ciudad = sociallogin.account.extra_data['hometown']['name'] Seville, Spain 
            
            user.first_name = sociallogin.account.extra_data['first_name']
            user.last_name = sociallogin.account.extra_data['last_name']
 
        if sociallogin.account.provider == 'google':
            perfil, creado = Perfil.objects.get_or_create(user=user)
            perfil.nombre = sociallogin.account.extra_data['given_name']
            perfil.apellidos = sociallogin.account.extra_data['family_name']
            #perfil.genero = sociallogin.account.extra_data['gender']
            
            user.first_name = sociallogin.account.extra_data['given_name']
            user.last_name = sociallogin.account.extra_data['family_name']
 
        user.save()
        perfil.save()
        
class Conocimiento(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50,
                                      choices=NIVELES,
                                      default='Básico')
    perfil = models.ForeignKey(Perfil, related_name="techs")
    
    def __unicode__(self):
        return '%s' % (self.nombre)


    