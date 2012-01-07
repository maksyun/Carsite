# -*- coding: utf8 -*-

from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView


class UslugiIndex(ListView):
	context_object_name = 'uslugi',
	template_name = 'templates/uslugi_list.html',
