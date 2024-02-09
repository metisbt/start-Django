from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Comment
from django.utils import timezone
from datetime import datetime, timezone
from blog.forms import CommentForm
from django.contrib import messages



def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=datetime.now(tz=timezone.utc), status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])

    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except EmptyPage:
        posts = posts.page(1)
    except PageNotAnInteger:
        posts = posts.page(1)

    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your comment has sent successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Your comment send failed!")
            
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

    comment = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
    form = CommentForm()

    context = {
        'post' : post,
        'next_post' : next_post,
        'prev_post' : prev_post,
        'comment' : comment,
        'form' : form
               }
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts= posts.filter(content__contains=s)

    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)