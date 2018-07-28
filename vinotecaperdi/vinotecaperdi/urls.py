"""vinotecaperdi URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from vinotecaperdi.addwine import views as addwine_views
from vinotecaperdi.core import views as core_views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^addwine/$', addwine_views.addnewwine, name='addwine'),
    url(r'^mywines/$', addwine_views.listwineuser, name='mywines'),
    url(r'^thanks/$', addwine_views.thanks, name='thanks'),
    url(r'^votes/$', addwine_views.WineListView, name='votes'),
    url(r'^vote/$',addwine_views.RateWine, name='vote'),
    url(r'^ranking/$', addwine_views.ranking, name='ranking')

]
