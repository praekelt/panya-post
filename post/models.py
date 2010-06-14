from panya.models import ModelBase
from ckeditor.fields import RichTextField

class Post(ModelBase):
    content = RichTextField(
        blank=True,
        null=True,
    )

    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
