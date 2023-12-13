from django.contrib import admin
from django.urls import path
from note import views

app_name = 'note_app'

urlpatterns = [
    path('home/note/',views.note)
]
