from django.conf.urls import url,include
from app import views

urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^create_bug/$', views.new_bug, name='submit_bug'),
]
