from django.shortcuts import render
from .models import LectureMpdel

def lecture(request):
    if request.method=="POST":
        # print('POSTリクエストが来ました！')
        # print(request.POST)
        models = LectureMpdel.objects.filter(name=request.POST['searchValue'])
        return render(request, "lecture.html", context={'models':models})
    return render(request,"lecture.html")