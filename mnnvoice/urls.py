from django.contrib import admin
from django.urls import path
from mnnvoice import views

app_name = 'mnnvoice_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',views.index, name='mnnvoice_home'),
    path('home/mnnvoice/',views.mnnvoice),
    path('home/search/',views.search)
]
