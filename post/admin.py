from django.contrib import admin

from content.models import ModelAdminBase
from post.models import Post


admin.site.register(Post, ModelAdminBase)