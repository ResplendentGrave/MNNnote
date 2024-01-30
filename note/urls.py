from django.contrib import admin
from django.urls import path
from note import views

app_name = 'note_app'

urlpatterns = [
    path('',views.note, name="note_base"),
    #path('upload/',views.note),
]
