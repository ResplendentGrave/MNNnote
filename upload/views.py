from django.shortcuts import render, redirect
from .forms import UploadForm

# Create your views here.
def upload(request):
    forms = UploadForm()

    """もしリクエストがPOSTの場合"""
    if request.method == "POST":
        forms = UploadForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            forms.save()
        return redirect("/home/#note")

    return render(request,"upload.html", context={
        'forms': forms,
    })