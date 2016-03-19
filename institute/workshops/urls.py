from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^workshops/$', views.topic_list, name='topic_list'),
    # ex: /workshops/5/
    url(r'^workshops/(?P<topic_id>[0-9]+)/$', views.topic_detail, name='topic_detail'),
    
]

