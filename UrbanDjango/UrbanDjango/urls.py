"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('example1/', include('example1.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import ClassView, func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', ClassView.as_view(), name='class_template'),
    path('func/', func, name='func_template'),
]

from django.contrib import admin
from django.urls import path
from task3.views import platform, games, cart

urlpatterns = [
    path('', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
]