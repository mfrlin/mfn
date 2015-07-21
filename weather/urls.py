from django.conf.urls import url

from . import views

urlpatterns = [
	url('^$', views.simple_chart, name='simple_chart'),
]