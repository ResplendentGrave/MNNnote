from django.urls import path, include

"""media用の設定"""
from django.conf import settings
from django.conf.urls.static import static
# regist your apps in this file like 
# path('', include('[appname].urls'))
urlpatterns = [
    path('', include('userlogapp.urls')),
    path('home/', include('mnnvoice.urls')),
    path('home/lecture/',include('lecture.urls')),
    path('home/note/',include('note.urls')),
    path('home/upload/',include('upload.urls')),
]

#開発の時はこれを記入する
if settings.DEBUG:
    urlpatterns+= static( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


