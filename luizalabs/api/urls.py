from django.conf.urls import patterns, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # url(r'^/$', 'luizalabs.views.home', name='home'),

                       url(r'^persons/', views.PersonList.as_view()),
                       url(r'^person/(?P<facebook_id>[0-9]+)/$',
                           views.PersonDetail.as_view()),
                       )
