from django.conf.urls import url

from .views import *
# from .views import blog_home, article_detail, article_create, article_delete, \
                #    article_update


urlpatterns = [

    url(r'^$', myadmin_home, name="myadmin-home"),
    url(r'^all/$', myadmin_all, name="myadmin-all"),
    url(r'^add/$', myadmin_add, name="myadmin-add"),
    url(r'^delete/$', myadmin_delete, name="myadmin-delete"),
    url(r'^(?P<model_name>\w+)/$', myadmin_list_model, name="myadmin-models-list"),
    # url(r'^(?P<model_name>\w+)/update/(?P<pk>\d+)/$', myadmin_update, name="myadmin-update"),
    url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/$', myadmin_detail, name="myadmin-detail"),
    url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/delete$', myadmin_object_delete, name="myadmin-deletator"),
    url(r'^(?P<model_name>\w+)/create/$', myadmin_object_create, name="myadmin-creator"),
    url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/update$', myadmin_object_update, name="myadmin-update"),

    # url(r'^(?P<model_name>\w+)/(?P<pk>\d+)/$', person_detail, name="person-detail"),

#
#     url(r'^create/$', article_create, name="article-create"),
#     url(r'^delete/(?P<pk>\d+)/$', article_delete, name="article-delete"),
#     url(r'^update/(?P<pk>\d+)/$', article_update, name="article-update"),
]
