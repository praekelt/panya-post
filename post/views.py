from django.core.urlresolvers import reverse

from post.models import Post
from panya.generic.views import GenericObjectDetail, GenericObjectList 
from panya.view_modifiers import DefaultViewModifier

class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Posts'}
        
    def get_view_modifier(self, request, *args, **kwargs):
        return DefaultViewModifier(request, *args, **kwargs)

    def get_paginate_by(self, *args, **kwargs):
        return 12
    
    def get_queryset(self, *args, **kwargs):
        return Post.permitted.all()

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_queryset(self, *args, **kwargs):
        return Post.permitted.all()
    
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Posts'}
    
    def get_view_modifier(self, request, *args, **kwargs):
        return DefaultViewModifier(request, base_url=reverse("post_object_list"), ignore_defaults=True, *args, **kwargs)
    
object_detail = ObjectDetail()
