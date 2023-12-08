from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def mnnvoice(request):
    return render(request,"mnnvoice.html")