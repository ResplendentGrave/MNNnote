from django.urls import path, include
# regist your apps in this file like 
# path('', include('[appname].urls'))
urlpatterns = [
    path('', include('userlogapp.urls')),
    #path('', include('mnnvoice.urls')),
]
