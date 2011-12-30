from django import template
from news.models import CarNews
register = template.Library()

@register.inclusion_tag('s_news.html')
def news():
	news = CarNews.objects.all().order_by('-created')[0:4]
	return { 'news' : news }
	
	
