from django.shortcuts import render
from django.views import generic
from .models import Post


# The code taken from the Code Institute Django3blog project
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3

def about(request):
    return render(request, 'about.html', {'title': 'About'})