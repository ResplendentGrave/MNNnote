from django.shortcuts import render
from .forms import UploadForm

# Create your views here.
def upload(request):
    forms = UploadForm()
    return render(request,"upload.html", context={
        'forms': forms,
    })