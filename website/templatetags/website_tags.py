from django import template
from blog.models import Post
from django.utils import timezone
from datetime import datetime, timezone

register = template.Library()

@register.inclusion_tag('website/latest-post-home.html')
def latest_post_home():
    posts = Post.objects.filter(published_date__lte=datetime.now(tz=timezone.utc), status=1).order_by('-published_date')[:6]
    return {'posts' : posts}
