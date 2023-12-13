from django.contrib import admin
from django.urls import path
from lecture import views

app_name = 'lecture_app'

urlpatterns = [
    path('',views.lecture)
]
