from django.conf.urls import patterns, include, url
from django.contrib import admin
from locacao import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
