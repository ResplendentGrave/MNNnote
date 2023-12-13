from django.shortcuts import render

def lecture(request):
    return render(request,"lecture.html")