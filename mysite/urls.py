"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from mysite.views import home 
from mysite.views import about
from mysite.views import contact
from mysite.views import detail_artikel
from mysite.authentikasi import akun_login, akun_registrasi, akun_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('detail/<int:id>', detail_artikel, name="detail_artikel"),

    path('dashboard/', include("berita.urls")),

    path('authentikasi/login', akun_login, name="akun_login"),
    path('authentikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/logout', akun_logout, name="akun_logout"),


]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)