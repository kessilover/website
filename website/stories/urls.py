from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^index/$', views.home, name="index"),
    url(r'^tlp/$', views.affichage),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)