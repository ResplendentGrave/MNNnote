from django.shortcuts import render
from .models import LectureMpdel

def lecture(request):
    if request.method=="POST":
        if request.POST["searchValue"] == "":
            return render(request, "lecture.html")
        models = LectureMpdel.objects.filter(name__contains=request.POST['searchValue'])
        return render(request, "lecture.html", context={'models':models})
    return render(request,"lecture.html")