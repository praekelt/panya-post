from copy import deepcopy

from django import forms
from django.contrib import admin

from content.admin import ContentBaseAdmin
from post.models import Post
from ckeditor.widgets import CKEditorWidget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post

class PostAdmin(ContentBaseAdmin):
    #form = PostAdminForm
    fieldsets = deepcopy(ContentBaseAdmin.fieldsets)
    for fieldset in fieldsets:
        if fieldset[0] == None:
            fieldset[1]['fields'] += ('content',)

admin.site.register(Post, PostAdmin)
