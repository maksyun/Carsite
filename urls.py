# -*- coding: utf8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, DeleteView
from carsite.news.views import CarNewsIndex
from carsite.news.models import CarNews
from carsite.uslugi.models import Uslugi
from carsite.uslugi.views import UslugiIndex
from django.contrib import admin
from django.conf import settings
from carsite.views import contact

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^tunymce/', include('tinymce.urls')),
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='index_page'),
    url(r'^contact/$', 'carsite.views.contact', name='contact'),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}, name='about'),
    url(r'^contact/thanks/$', direct_to_template, {'template': 'thanks.html'}, name='contact'),
    url(r'^news/$', ListView.as_view(
									model = CarNews,
									template_name = 'carnews_list.html',
									), name='news_page'),
	url(r'^news/(?P<slug>[-\w]+)/$', DetailView.as_view(
									model = CarNews,
									template_name = 'carnews_detail.html',
									), name='single_news'),
    url(r'^uslugi/$', ListView.as_view(
									model = Uslugi,
									template_name = 'uslugi_list.html',
									), name='uslugi_page'),
	url(r'^uslugi/(?P<slug>[-\w]+)/$', DetailView.as_view(
									model = Uslugi,
									template_name = 'uslugi_detail.html',
									), name='single_uslugi'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':'/home/maks/mysite/carsite/media/'}),
	
	
)
