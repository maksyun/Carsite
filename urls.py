# -*- coding: utf8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView, ListView, DeleteView
from carsite.news.views import CarNewsIndex
from carsite.news.models import CarNews
from django.core.paginator import Paginator
from django.contrib import admin
from django.conf import settings
#from filebrowser.sites import site
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^admin/filebrowser/', include(site.urls)),
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/filebrowser/', include('filebrowser.urls')),
	url(r'^tunymce/', include('tinymce.urls')),
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='index_page'),
    url(r'^news/$', ListView.as_view(
									model = CarNews,
									template_name = 'carnews_list.html',
									paginate_by = 10,
									paginator_class = Paginator
									), name='news_page'),
	url(r'^news/(?P<slug>[-\w]+)/$', DetailView.as_view(
									model = CarNews,
									template_name = 'carnews_detail.html',
									), name='single_news'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':'/home/maks/mysite/carsite/media/'}),
	
	
)
