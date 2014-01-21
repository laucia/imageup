import os
import shutil

from django.test import TestCase
from django.conf import settings
from imageup.models import UploadedImage

class ImageUpload(TestCase):
	def setUp(self):
		self.TEST_ROOT = os.path.dirname(os.path.realpath(__file__))

		# Change MEDIA_ROOT
		self._old_MEDIA_ROOT = settings.MEDIA_ROOT
		settings.MEDIA_ROOT = self.TEST_ROOT

	def tearDown(self):
		# reset MEDIA_ROOT
		settings.MEDIA_ROOT = self._old_MEDIA_ROOT

	def test_delete_image(self):
		'''
		Test for the removal of actual files when removing 
		database references

		'''
		test_image = os.path.join(
			self.TEST_ROOT,
			'test.png'
			)
		test_image_copy = os.path.join(
			self.TEST_ROOT,
			'test_cp.png'
			)
		shutil.copy2(test_image,test_image_copy)

		up = UploadedImage.objects.create(
			title="test",
			image=test_image_copy,
			description="this is a test description"
			)
		up.delete()

		self.assertFalse(os.path.exists(test_image_copy))



	def test_modify_image(self):
		'''
		Test for the replacement of actual files when changing 
		database references
		
		'''
		test_image = os.path.join(
			self.TEST_ROOT,
			'test.png'
			)
		test_image_copy1 = os.path.join(
			self.TEST_ROOT,
			'test_cp.png'
			)
		test_image_copy2 = os.path.join(
			self.TEST_ROOT,
			'test_cp2.png'
			)

		shutil.copy2(test_image,test_image_copy1)
		shutil.copy2(test_image,test_image_copy2)
		
		up = UploadedImage.objects.create(
			title="test",
			image=test_image_copy1,
			description="this is a test description"
			)

		up.image = test_image_copy2
		up.save()
		self.assertFalse(os.path.exists(test_image_copy1))

		up.delete()
		self.assertFalse(os.path.exists(test_image_copy2))


