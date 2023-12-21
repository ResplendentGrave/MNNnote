from django.contrib import admin
from django.urls import path
from note import views

app_name = 'note_app'

urlpatterns = [
    path('',views.note),
    #path('upload/',views.note),
]
