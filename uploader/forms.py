# uploader/forms.py

from django import forms

class UploadedFileForm(forms.Form):
    file = forms.FileField()
