from django import forms
from.models import imageupload

class imageform(forms.ModelForm):
    class Meta:
        model=imageupload
        fields=['image']