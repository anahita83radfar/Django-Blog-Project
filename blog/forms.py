from .models import Comment, Post
from django import forms
from django.utils.text import slugify
from django.core.exceptions import ValidationError


# The code taken from the Code Institute Django3blog project
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        data = self.cleaned_data['title']

        slug = slugify(data)

        if Post.objects.filter(slug=slug).exists():
            raise ValidationError('A question with this title already exists.')

        return data

