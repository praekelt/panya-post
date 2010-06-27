from django.core.urlresolvers import reverse
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
    
    def get_absolute_url(self):
        return reverse('post_object_detail', kwargs={'slug': self.slug})
