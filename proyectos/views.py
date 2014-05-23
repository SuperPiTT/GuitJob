from django import http
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from principal.views import slugify
from proyectos.forms import ProyectoForm
from proyectos.models import Proyecto


# Create your views here.
class ProyectoDetailView(DetailView):
    template_name="proyectos/detalle.html"
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    

class ProyectoListView(ListView):
    template_name="proyectos/lista.html"
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context
    
#class ProyectoCreateView(CreateView):
#    template_name="proyectos/crear.html"
#    model = Proyecto
#    fields = ['name']

class ProyectoCreateView(CreateView):
    form_class = ProyectoForm
    template_name = 'proyectos/crear.html'
    #success_url = 'success'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        form.instance.slug = slugify(form.instance.titulo)
        return super(ProyectoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProyectoCreateView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    