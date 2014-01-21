# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadedImage'
        db.create_table(u'imageup_uploadedimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('width', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'imageup', ['UploadedImage'])


    def backwards(self, orm):
        # Deleting model 'UploadedImage'
        db.delete_table(u'imageup_uploadedimage')


    models = {
        u'imageup.uploadedimage': {
            'Meta': {'object_name': 'UploadedImage'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['imageup']