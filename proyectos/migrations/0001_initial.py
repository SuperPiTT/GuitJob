# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoProyecto'
        db.create_table(u'proyectos_tipoproyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'proyectos', ['TipoProyecto'])

        # Adding model 'Tecnologia'
        db.create_table(u'proyectos_tecnologia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'proyectos', ['Tecnologia'])

        # Adding model 'Rol'
        db.create_table(u'proyectos_rol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'proyectos', ['Rol'])

        # Adding model 'NivelRol'
        db.create_table(u'proyectos_nivelrol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'proyectos', ['NivelRol'])

        # Adding model 'VotoIdea'
        db.create_table(u'proyectos_votoidea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voto', self.gf('django.db.models.fields.IntegerField')()),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'proyectos', ['VotoIdea'])

        # Adding model 'Idea'
        db.create_table(u'proyectos_idea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'proyectos', ['Idea'])

        # Adding M2M table for field votos on 'Idea'
        m2m_table_name = db.shorten_name(u'proyectos_idea_votos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('idea', models.ForeignKey(orm[u'proyectos.idea'], null=False)),
            ('votoidea', models.ForeignKey(orm[u'proyectos.votoidea'], null=False))
        ))
        db.create_unique(m2m_table_name, ['idea_id', 'votoidea_id'])

        # Adding model 'EstadoTarea'
        db.create_table(u'proyectos_estadotarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proyectos', ['EstadoTarea'])

        # Adding model 'Tarea'
        db.create_table(u'proyectos_tarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('info', self.gf('django.db.models.fields.TextField')(max_length=150, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.EstadoTarea'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'proyectos', ['Tarea'])

        # Adding model 'Proyecto'
        db.create_table(u'proyectos_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creador', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('info', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('repo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('docu', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.TipoProyecto'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'proyectos', ['Proyecto'])

        # Adding M2M table for field techs on 'Proyecto'
        m2m_table_name = db.shorten_name(u'proyectos_proyecto_techs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'proyectos.proyecto'], null=False)),
            ('tecnologia', models.ForeignKey(orm[u'proyectos.tecnologia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'tecnologia_id'])

        # Adding M2M table for field ideas on 'Proyecto'
        m2m_table_name = db.shorten_name(u'proyectos_proyecto_ideas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'proyectos.proyecto'], null=False)),
            ('idea', models.ForeignKey(orm[u'proyectos.idea'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'idea_id'])

        # Adding M2M table for field siguiendo on 'Proyecto'
        m2m_table_name = db.shorten_name(u'proyectos_proyecto_siguiendo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'proyectos.proyecto'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'user_id'])

        # Adding M2M table for field tareas on 'Proyecto'
        m2m_table_name = db.shorten_name(u'proyectos_proyecto_tareas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm[u'proyectos.proyecto'], null=False)),
            ('tarea', models.ForeignKey(orm[u'proyectos.tarea'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proyecto_id', 'tarea_id'])

        # Adding model 'Equipo'
        db.create_table(u'proyectos_equipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proyecto_equipo', to=orm['proyectos.Proyecto'])),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Rol'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'proyectos', ['Equipo'])

        # Adding model 'Buscando'
        db.create_table(u'proyectos_buscando', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos.Rol'])),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proyecto_buscando', to=orm['proyectos.Proyecto'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'proyectos', ['Buscando'])


    def backwards(self, orm):
        # Deleting model 'TipoProyecto'
        db.delete_table(u'proyectos_tipoproyecto')

        # Deleting model 'Tecnologia'
        db.delete_table(u'proyectos_tecnologia')

        # Deleting model 'Rol'
        db.delete_table(u'proyectos_rol')

        # Deleting model 'NivelRol'
        db.delete_table(u'proyectos_nivelrol')

        # Deleting model 'VotoIdea'
        db.delete_table(u'proyectos_votoidea')

        # Deleting model 'Idea'
        db.delete_table(u'proyectos_idea')

        # Removing M2M table for field votos on 'Idea'
        db.delete_table(db.shorten_name(u'proyectos_idea_votos'))

        # Deleting model 'EstadoTarea'
        db.delete_table(u'proyectos_estadotarea')

        # Deleting model 'Tarea'
        db.delete_table(u'proyectos_tarea')

        # Deleting model 'Proyecto'
        db.delete_table(u'proyectos_proyecto')

        # Removing M2M table for field techs on 'Proyecto'
        db.delete_table(db.shorten_name(u'proyectos_proyecto_techs'))

        # Removing M2M table for field ideas on 'Proyecto'
        db.delete_table(db.shorten_name(u'proyectos_proyecto_ideas'))

        # Removing M2M table for field siguiendo on 'Proyecto'
        db.delete_table(db.shorten_name(u'proyectos_proyecto_siguiendo'))

        # Removing M2M table for field tareas on 'Proyecto'
        db.delete_table(db.shorten_name(u'proyectos_proyecto_tareas'))

        # Deleting model 'Equipo'
        db.delete_table(u'proyectos_equipo')

        # Deleting model 'Buscando'
        db.delete_table(u'proyectos_buscando')


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
            'creador': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
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