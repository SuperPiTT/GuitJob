from django.core.urlresolvers import reverse
from django.db import models

from guitjob import settings


class TipoProyecto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return '%s' % (self.nombre)
    
class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __unicode__(self):
        return '%s' % (self.nombre)
    
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return '%s' % (self.nombre)

class NivelRol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return '%s' % (self.nombre)
    
class VotoIdea(models.Model):
    voto = models.IntegerField()
    usuario  = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return '%s' % (self.nombre)

class Idea(models.Model):
    desc = models.CharField(max_length=150, unique=True)
    votos = models.ManyToManyField(VotoIdea)
    usuario  = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return '%s' % (self.desc)

class EstadoTarea(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % (self.nombre)
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=30)
    info = models.TextField(max_length=150, blank=True, null=True)
    estado = models.ForeignKey(EstadoTarea)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s' % (self.titulo)
# Create your models here.
class Proyecto(models.Model):
    creador = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = models.SlugField(unique=True)
    titulo = models.CharField(max_length=50)
    slogan = models.CharField(max_length=75, blank=True, null=True)
    desc = models.CharField(max_length=150)
    info = models.TextField(max_length=500, blank=True, null=True)
    repo = models.URLField(blank=True, null=True)
    web = models.URLField(blank=True, null=True)
    docu = models.URLField(blank=True, null=True)
    
    tipo = models.ForeignKey(TipoProyecto)
    techs = models.ManyToManyField(Tecnologia)
    equipo = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Equipo', related_name="proyectos")
    buscando = models.ManyToManyField(Rol, through='Buscando', related_name="roles")
    ideas = models.ManyToManyField(Idea, related_name="ideaproyecto")
    siguiendo = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="siguiendo")
    tareas = models.ManyToManyField(Tarea)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s' % (self.titulo)
    def get_absolute_url(self):
            return reverse('proyectos_detalle', kwargs={'slug': self.slug})

class Equipo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    proyecto =  models.ForeignKey(Proyecto, related_name="proyecto_equipo")
    rol = models.ForeignKey(Rol)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    
class Buscando(models.Model):
    rol = models.ForeignKey(Rol)
    proyecto =  models.ForeignKey(Proyecto, related_name="proyecto_buscando")
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
