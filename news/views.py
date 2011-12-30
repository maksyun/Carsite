# -*- coding: utf8 -*-

from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.core.paginator import Paginator

class CarNewsIndex(ListView):
	context_object_name = 'news_page',
	template_name = 'templates/carnews_list.html',
	paginate_by = 10
	paginate_class = Paginator
	


