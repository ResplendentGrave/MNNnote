from django.contrib import admin
from django.urls import path
from mnnvoice import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',views.index),
    path('home/mnnvoice/',views.mnnvoice)
]
