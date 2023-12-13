from django.urls import path, include
# regist your apps in this file like 
# path('', include('[appname].urls'))
urlpatterns = [
    path('', include('userlogapp.urls')),
    path('home/', include('mnnvoice.urls')),
    path('home/lecture/',include('lecture.urls')),
    path('home/note/',include('note.urls')),
]
