from django.contrib import admin
from imageup.models import *

class UploadedImageAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'image', )
		}),
		('Options', {
			'classes': ('collapse',),
			'fields': ('description',)
		}),
	)
	list_display = ('title','url')
	search_fields = ['title',]


admin.site.register(UploadedImage,UploadedImageAdmin)
