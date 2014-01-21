import os

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy as _

def get_image_path(instance, filename):
	'''
	Utility function for naming

	'''

	ext = filename.split('.')[-1]
	name = u'%s.%s' % (instance.title, ext)
	return os.path.join('images', name)

class UploadedImage(models.Model):
	'''
	Simple class to upload images to the server

	'''

	# Fields
	# - - - - - - - - - - - - - - - - - - - - - -
	title = models.CharField(
		max_length = 60,
		unique = True,
		verbose_name = _(u'title'),
		)
	image = models.ImageField(
		upload_to = get_image_path,
		verbose_name = _(u'image'),
		)
	description = models.TextField(
		blank=True,
		null=True,
		verbose_name = _(u'description')
		)

	# Verbose
	# - - - - - - - - - - - - - - - - - - - - - -
	def __unicode__(self):
		return self.title

	# Meta
	# - - - - - - - - - - - - - - - - - - - - - -
	class Meta:
		ordering = ['title',]
		verbose_name=_(u'uploaded image')
		verbose_name_plural = _(u'uploaded images')

	# Functions
	# - - - - - - - - - - - - - - - - - - - - - -
	def url(self):
		return self.image.url