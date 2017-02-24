from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.home, name="index"),
    url(r'^tlp/(?P<id>\d+)$', views.affichage),

]