from django import template
from django.db.models import Count
from ..models import Post

register = template.Library()
@register.inclusion_tag('blog/posts/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}
@register.inclusion_tag('blog/posts/most_commented_posts.html')
def get_most_commented_posts(count=5):
    most_commented_posts = Post.objects.annotate(num_comment=Count('comments')).order_by('-num_comment')[:count]
    return {'most_commented_posts':most_commented_posts}

