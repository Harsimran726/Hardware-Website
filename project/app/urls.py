"""
URL configuration for project project.

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
from app import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path("",views.index,name="Home Page"),
    path("products",views.products,name="Products"),
    path("index",views.index,name="Product Filter"),
    path("contact",views.contact,name="Contact"),
    path("contacted",views.contacted,name="Contact"),
    path("about",views.about,name='About'),
    path("<str:slug>", views.product_detail, name="Product Page"),

]