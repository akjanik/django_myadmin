from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^$', myadmin_home, name="myadmin-home"),
    url(r'^all/$', myadmin_all, name="myadmin-all"),
    url(r'^add/$', myadmin_add, name="myadmin-add"),
    url(r'^delete/(?P<model_name>\w+)$', myadmin_delete, name="myadmin-delete"),

    url(r'^(?P<model_name>\w+)/$', myadmin_object_list, name="myadmin-object-list"),
    url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/$', myadmin_detail, name="myadmin-detail"),
    url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/delete$', myadmin_object_delete, name="myadmin-deletator"),
    url(r'^(?P<model_name>\w+)/create/$', myadmin_object_create, name="myadmin-creator"),
    url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/update$', myadmin_object_update, name="myadmin-update"),

]
