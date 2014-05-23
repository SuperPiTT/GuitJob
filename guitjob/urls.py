from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from guitjob import settings
from principal.views import IndexView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guitjob.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cuentas/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^cuentas/', include('allauth.urls')),
    url(r'^perfiles/', include('perfiles.urls')),
    url(r'^proyectos/', include('proyectos.urls')),
    url(r'^$', IndexView.as_view() ,name="index"),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
