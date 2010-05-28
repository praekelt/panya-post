from django.contrib import admin

from content.admin import ModelBaseAdmin
from post.models import Post

admin.site.register(Post, ModelBaseAdmin)
