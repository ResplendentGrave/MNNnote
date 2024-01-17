from django import forms

from .models import UploadModel

class UploadForm(forms.ModelForm):
    note_title = forms.CharField(label='ノートタイトル')
    file       = forms.FileField(label='ノートをアップロード')

    class Meta:
        model = UploadModel
        fields = ["note_title", "create_user", "file", "lecture_choice", "lecture_model"]
    