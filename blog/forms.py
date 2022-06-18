from .models import Comment
from django import forms


# The code taken from the Code Institute Django3blog project
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        