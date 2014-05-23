from django.contrib import admin

from proyectos.models import Tecnologia, TipoProyecto, Rol, NivelRol


# Register your models here.
admin.site.register(Tecnologia)
admin.site.register(TipoProyecto)
admin.site.register(Rol)
admin.site.register(NivelRol)

