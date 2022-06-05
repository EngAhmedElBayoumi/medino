from dataclasses import field, fields
from django import forms
from .models import Post,Comment


#

class blog_form(forms.ModelForm):
    class Meta:
        model = Post
        fields='__all__'
        exclude=('slug','create_by',)


class commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('message',)
        