from django.conf.urls import patterns, url

from perfiles.views import PerfilListView, PerfilDetailView, PerfilUpdateView, \
    EditarConocimientoView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guitjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^(?P<pk>[0-9]+)$', PerfilDetailView.as_view(), name="perfiles_detalle"),
    url(r'^(?P<pk>[0-9]+)/editar$', PerfilUpdateView.as_view(), name="perfiles_informacion_editar"),
    url(r'^(?P<pk>[0-9]+)/editar-conocimiento$', EditarConocimientoView.as_view() , name="perfiles_informacion_editar_conocimiento"),
    url(r'^lista$', PerfilListView.as_view(), name="perfiles_lista"),
)
