from django.contrib.syndication.views import Feed
from .models import Post
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy


class LatestPostFeed(Feed):
    title='My Blog'
    link = reverse_lazy('blog:post_list')
    description ='My post feed'
    def items(self):
        return Post.objects.all()
    def item_title(self,obj):
        return obj.title 
    def item_description(self,obj):
        return truncatewords(obj.body,30)