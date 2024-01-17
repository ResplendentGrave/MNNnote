from django import forms

class UploadForm(forms.Form):
    name = forms.CharField()
    note_title = forms.CharField()
    file = forms.FileField()