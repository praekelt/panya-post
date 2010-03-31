from copy import deepcopy

from django.contrib import admin

from content.admin import ContentBaseAdmin
from post.models import Post

class PostAdmin(ContentBaseAdmin):
    fieldsets = deepcopy(ContentBaseAdmin.fieldsets)
    for fieldset in fieldsets:
        if fieldset[0] == None:
            fieldset[1]['fields'] += ('content',)

admin.site.register(Post, PostAdmin)
