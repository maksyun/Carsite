# -*- coding: utf8 -*-

from django.db import models
from django import forms
import datetime
from django.db.models import permalink
from tinymce import models as tinymce_models


class CarNews(models.Model):
    STATUS_CHOICES = (
        (1, 'На редакции'),
        (2, 'Опубликовано'),
        (3, 'В архив'),    
    )
    title = models.CharField('Заголовок', max_length=100, null=False, blank=False)
    slug = models.SlugField('Ссылка', unique=True, null=False, blank=False, max_length=150)
    content = tinymce_models.HTMLField()  
    status = models.IntegerField('Статус', choices = STATUS_CHOICES, default=1, null=False, blank=False)
    created = models.DateTimeField('Создано', default=datetime.datetime.now, null=False, blank=False)
    modified = models.DateTimeField('Изменено', default=datetime.datetime.now, null=False, blank=False)

    class Meta:
        ordering = ['created']
        
         
    @models.permalink
    def get_absolute_url(self):
        return ('single_news', [str(self.slug)])
        
