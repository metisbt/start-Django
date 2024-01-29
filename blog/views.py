from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    posts = Post.objects.all()

    for post in posts:
        if post.published_date <= timezone.now():
            post.status = True
        else:
            continue

    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, id = pid)
    post.counted_view += 1
    context = {'post' : post}
    return render(request, 'blog/blog-single.html', context)