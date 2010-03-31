from django.db import models
from content.models import ContentBase

from ckeditor.fields import RichTextField

class Post(ContentBase):
    content = RichTextField()

    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
