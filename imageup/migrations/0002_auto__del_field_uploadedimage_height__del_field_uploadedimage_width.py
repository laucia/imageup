# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UploadedImage.height'
        db.delete_column(u'imageup_uploadedimage', 'height')

        # Deleting field 'UploadedImage.width'
        db.delete_column(u'imageup_uploadedimage', 'width')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'UploadedImage.height'
        raise RuntimeError("Cannot reverse this migration. 'UploadedImage.height' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'UploadedImage.width'
        raise RuntimeError("Cannot reverse this migration. 'UploadedImage.width' and its values cannot be restored.")

    models = {
        u'imageup.uploadedimage': {
            'Meta': {'object_name': 'UploadedImage'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        }
    }

    complete_apps = ['imageup']