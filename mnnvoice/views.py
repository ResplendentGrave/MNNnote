from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def mnnvoice(request):
    return render(request,"mnnvoice.html")

def search(request):
    return render(request,"search.html")

def reloc(request):
    print(request.GET.get("auth"))
    username=request.user
    # print(username,type(username))
    if username.is_authenticated:
        print('true') 
    else: 
        print('false')
    if request.method == 'POST':
        print(request)
        return JsonResponse({
            "data":{
                "id":"1",
                "a":"99"
            },
            "state":200,

        })
    else:
        return JsonResponse({
            "state":404,
            "message":"没有找到该资源"
        })