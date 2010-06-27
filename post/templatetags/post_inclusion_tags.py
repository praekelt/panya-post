from django import template

register = template.Library()

@register.inclusion_tag('post/inclusion_tags/post_listing.html')
def post_listing(object_list):
    return {'object_list': object_list}

@register.inclusion_tag('post/inclusion_tags/post_detail.html')
def post_detail(obj):
    return {'object': obj}
