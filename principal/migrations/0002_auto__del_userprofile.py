# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'principal_userprofile')


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'principal_userprofile', (
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cumple', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'principal', ['UserProfile'])


    models = {
        
    }

    complete_apps = ['principal']