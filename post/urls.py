from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'post.views',
    url(r'^list/$', 'object_list', name='post_object_list'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='post_object_detail'),
)
