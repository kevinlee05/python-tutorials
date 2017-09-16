from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

urlpatterns =[
    #post views - functional view
    url(r'^$', views.post_list_functional, name='post_list_functional'),
    #class based list view
    url(r'^list_class_based$', views.PostListView.as_view(), name='post_list'),
    # post list filtered by tag
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list_functional, name='post_list_by_tag'),
    # individual post view
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    # share post view
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    # latest posts feed view
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),

]