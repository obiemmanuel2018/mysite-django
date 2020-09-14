from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse




class Post(models.Model):
      STATUS_CHOICE = (
        ('draft','Draft'),
        ('published','Published')
      )

      author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
      title = models.CharField(max_length=100)
      body = models.TextField()
      published_date = models.DateTimeField(blank=True,null=True)
      created_date =  models.DateTimeField(default=timezone.now)
      updated_date = models.DateTimeField(blank=True,null=True)
      status = models.CharField(max_length = 10,choices=STATUS_CHOICE,default='draft')
      number_of_views = models.PositiveIntegerField(default=0)
      image = models.ImageField(upload_to='post_images',null=False,blank=False,default='post_images/default_post.jpg')
      views = models.ManyToManyField(User,related_name='views',blank=True)
   

      def approved_comments(self):
          return self.comments.filter(approved_comment = True).order_by('created_date')

      def has_been_viewed(self):
          self.number_of_views = self.number_of_views + 1;
      def publish(self):
          self.published_date = timezone.now()
          self.status='published'
          self.save()

     
      def get_absolute_url(self):
          return reverse('blog:post_detail',args=[self.id])
      def __str__(self):
          return self.title



class UserProfileInfo(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      profile_pic = models.ImageField(upload_to='profile_pics',blank=True,default='profile_pics/default_profile.jpg')
      


class Comment(models.Model):
      
      post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
      author = models.CharField(max_length=200,blank=True)
      author_profile_pic = models.ImageField(null=True,default='profile_pics/default_profile.jpg')
      body = models.TextField(max_length=100)
      created_date = models.DateTimeField(default=timezone.now)
      approved_comment = models.BooleanField(default=False)
      
    



      def approve(self):
          self.approved_comment = True
          self.save()
      
      
      def __str__(self):
          return self.body
        
     






