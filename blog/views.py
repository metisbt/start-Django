from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone
from datetime import datetime, timezone


def blog_view(request):
    posts = Post.objects.filter(published_date__lte=datetime.now(tz=timezone.utc), status=True)
    
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    # posts = Post.objects.filter(published_date__lte=datetime.now(tz=timezone.utc), status=True)
    # post = get_object_or_404(posts, id = pid)
    post = get_object_or_404(Post, id = pid, published_date__lte=datetime.now(tz=timezone.utc), status=True)
    post.counted_view += 1
    post.save()
    context = {'post' : post}
    return render(request, 'blog/blog-single.html', context)