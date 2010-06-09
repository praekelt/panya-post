from django.contrib import admin

from panya.admin import ModelBaseAdmin
from post.models import Post

admin.site.register(Post, ModelBaseAdmin)
