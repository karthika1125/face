from django.contrib import admin

from.models import contact,imageupload
admin.site.register(contact)
from django.contrib import admin
from .models import imageupload

@admin.register(imageupload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('image', '__str__')  # Avoid calling __str__ directly in list_display
