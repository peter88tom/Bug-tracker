from django.conf.urls import url,include
from app import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'-projects', views.ProjectViewSet)
router.register(r'-bugs', views.ProjectBugViewSet)



urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^create_bug/$', views.new_bug, name='submit_bug'),
    url(r'^api', include(router.urls)),

]
