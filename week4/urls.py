"""week4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django_web.views import index
from django_web.search import search, search_form, search_post, test

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^search-form$', search_form),
    url(r'^search$', search),
    url(r'^search-post$', search_post),
    url(r'^test', test),
    url(r'', index),
]
