from django.conf.urls import patterns, include, url

from principal.views import IndexView
from proyectos.views import ProyectoDetailView, ProyectoListView, \
    ProyectoCreateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guitjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^detalle$', ProyectoDetailView.as_view(), name="proyectos_detalle"),
    url(r'^lista', ProyectoListView.as_view(), name="proyectos_lista"),
    url(r'^crear', ProyectoCreateView.as_view(), name="proyectos_crear"),
    url(r'^(?P<slug>[a-zA-Z0-9._-]+)$', ProyectoDetailView.as_view(), name="proyectos_detalle"),

)
