from django.contrib import admin
from django.urls import path
from mnnvoice import views

app_name = 'mnnvoice_app'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index, name='mnnvoice_home'),
    path('mnnvoice/',views.mnnvoice),
    path('search/',views.search),
    path('api/reloc',views.reloc),
]
