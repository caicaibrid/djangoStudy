"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app.views import index,add,add2
from login.views import login,addUser
from templateStudy.views import Home
from modelStudy.views import index as addform


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
    url(r'^addUser/',addUser),
    url(r'^$', index),
    url(r'^add/$', add,name='add'),
    url(r'^add/(\d+)/(\d+)/$', add2,name='add2'),
    url(r'^templateStudy/$',Home),
    url(r'^formPost/',addform)
]
