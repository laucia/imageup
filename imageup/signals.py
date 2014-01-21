import os

from django.db import models
from django.dispatch import receiver

from imageup.models import UploadedImage

@receiver(models.signals.post_delete, sender=UploadedImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    '''
    Deletes file from filesystem
    when corresponding ``UploadedImage`` object is deleted.
    
    '''
    
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=UploadedImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    '''
    Deletes file from filesystem
    when corresponding ``UploadedImage`` object is changed.
    
    '''
    
    if not instance.pk:
        return False

    try:
        old_image = UploadedImage.objects.get(pk=instance.pk).image
    except UploadedImage.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)