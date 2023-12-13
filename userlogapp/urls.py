from django.contrib import admin
from django.urls import path, include

from .views import   signupfunc, loginfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    # path('home/', include('mnnvoice.urls'), name='home'),
]
