from django.conf.urls import patterns, url
from heuslers import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^search', views.index, name='index'),
	url(r'^about', views.about, name='about'),
	url(r'^contact', views.contact, name='contact'),
	url(r'^thanks', views.thanks, name='thanks'),
	url(r'^material/(?P<material_name_url>\w+)/$', views.material, name='material'),
	)