from django.urls import path
from upload import views

app_name = 'upload_app'

urlpatterns = [
    path('',views.upload),
    #path('upload/',views.note),
]
