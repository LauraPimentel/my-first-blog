from django.shortcuts import render
from django.http import HttpResponse
# from django.utils import timezone
# from .models import Post

def index(request):
    return render(request, 'registro/index.html')

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
