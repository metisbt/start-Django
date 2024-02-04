from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone
from datetime import datetime, timezone


def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=datetime.now(tz=timezone.utc), status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    # posts = Post.objects.filter(published_date__lte=datetime.now(tz=timezone.utc), status=True)
    # post = get_object_or_404(posts, id = pid)
    post = get_object_or_404(Post, id = pid, published_date__lte=datetime.now(tz=timezone.utc), status=True)
    post.counted_view += 1
    post.save()
    try:
        next_post = post.get_next_by_created_date()
    except post.DoesNotExist:
        next_post = False

    try:
        prev_post = post.get_previous_by_created_date()
    except post.DoesNotExist:
        prev_post = False

    context = {
        'post' : post,
        'next_post' : next_post,
        'prev_post' : prev_post
               }
    return render(request, 'blog/blog-single.html', context)
