# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Proyecto', fields ['creador']
        db.delete_unique(u'proyectos_proyecto', ['creador_id'])


        # Changing field 'Proyecto.creador'
        db.alter_column(u'proyectos_proyecto', 'creador_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):

        # Changing field 'Proyecto.creador'
        db.alter_column(u'proyectos_proyecto', 'creador_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))
        # Adding unique constraint on 'Proyecto', fields ['creador']
        db.create_unique(u'proyectos_proyecto', ['creador_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'proyectos.buscando': {
            'Meta': {'object_name': 'Buscando'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyecto_buscando'", 'to': u"orm['proyectos.Proyecto']"}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.Rol']"})
        },
        u'proyectos.equipo': {
            'Meta': {'object_name': 'Equipo'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyecto_equipo'", 'to': u"orm['proyectos.Proyecto']"}),
            'rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.Rol']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'proyectos.estadotarea': {
            'Meta': {'object_name': 'EstadoTarea'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'proyectos.idea': {
            'Meta': {'object_name': 'Idea'},
            'desc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'votos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['proyectos.VotoIdea']", 'symmetrical': 'False'})
        },
        u'proyectos.nivelrol': {
            'Meta': {'object_name': 'NivelRol'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'buscando': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'roles'", 'symmetrical': 'False', 'through': u"orm['proyectos.Buscando']", 'to': u"orm['proyectos.Rol']"}),
            'creador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'docu': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'equipo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'proyectos'", 'symmetrical': 'False', 'through': u"orm['proyectos.Equipo']", 'to': u"orm['auth.User']"}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'ideaproyecto'", 'symmetrical': 'False', 'to': u"orm['proyectos.Idea']"}),
            'info': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'repo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'siguiendo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'siguiendo'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tareas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['proyectos.Tarea']", 'symmetrical': 'False'}),
            'techs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['proyectos.Tecnologia']", 'symmetrical': 'False'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.TipoProyecto']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'proyectos.rol': {
            'Meta': {'object_name': 'Rol'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'proyectos.tarea': {
            'Meta': {'object_name': 'Tarea'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proyectos.EstadoTarea']"}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'proyectos.tecnologia': {
            'Meta': {'object_name': 'Tecnologia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'proyectos.tipoproyecto': {
            'Meta': {'object_name': 'TipoProyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'proyectos.votoidea': {
            'Meta': {'object_name': 'VotoIdea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'voto': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['proyectos']