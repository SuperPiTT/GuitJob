from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from perfiles.forms import PerfilForm, ConocimientoFormSet, ConocimientoForm
from perfiles.models import Perfil


# Create your views here.
class PerfilDetailView(DetailView):
    template_name="perfiles/detalle.html"
    model = Perfil

    def get_context_data(self, **kwargs):
        context = super(PerfilDetailView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    

class PerfilListView(ListView):
    template_name="perfiles/lista.html"
    model = Perfil

    def get_context_data(self, **kwargs):
        context = super(PerfilListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context
    
class PerfilUpdateView(UpdateView):
    form_class = PerfilForm
    template_name = 'perfiles/editar.html'
    model = Perfil
    #success_url = 'success'

    #def form_valid(self, form):
        #context = self.get_context_data()
        #conocimiento_form = context['conocimiento_form']
        #if conocimiento_form.is_valid():
            #self.object = form.save()
            #conocimiento_form.instance = self.object
            #conocimiento_form.save()
            #return super(PerfilUpdateView, self).form_valid(form)
        #else:
            #return self.render_to_response(self.get_context_data(form=form))

    #def form_invalid(self, form):
        #return self.render_to_response(self.get_context_data(form=form))

    #def get_context_data(self, **kwargs):
        #context = super(PerfilUpdateView, self).get_context_data(**kwargs)
        #context['user'] = self.request.user
        #if self.request.POST:
            #context['conocimiento_form'] = ConocimientoFormSet(self.request.POST, instance=self.request.user.mperfil)
        #else:
            #context['conocimiento_form'] = ConocimientoFormSet(instance=self.request.user.mperfil)
        #return context


class EditarConocimientoView(View):
    template_name = 'perfiles/editar-conocimiento.html'

    def get(self, request, *args, **kwargs):
        formset = ConocimientoFormSet(instance=self.request.user.mperfil)
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = ConocimientoFormSet(request.POST, instance=request.user.mperfil)
        if formset.is_valid():
            # <process form cleaned data>
            formset.save()
            return HttpResponseRedirect(request.user.mperfil.get_absolute_url())

        return render(request, self.template_name, {'formset': formset})
    def get_context_data(self, **kwargs):
        context = super(EditarConocimientoView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    