from django.conf.urls import patterns, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # url(r'^/$', 'luizalabs.views.home', name='home'),

                       url(r'^$', views.home),
                       )
