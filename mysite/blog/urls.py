from django.urls import path
from blog import views

from .feeds import LatestPostFeed




app_name ='blog'


urlpatterns = [
   path('',views.Post_list,name='post_list'),
   path('post/',views.Post_list,name='post_list'),
   path('post/create',views.Post_create,name="post_create"),
   path('post/<post_id>',views.Post_detail,name='post_detail'),
   path('post/<post_id>/update',views.Post_update,name="post_update"),
   path('post/<post_id>/delete',views.Post_delete,name='post_delete'),
   path('draft/<post_id>/delete',views.Draft_delete,name='draft_delete'),
   path('draft/<post_id>/publish',views.Draft_publish,name='draft_publish'),
   path('post/approve_comment/<comment_id>',views.approve_comment,name='approve_comment'),
   path('post/remove_comment/<comment_id>',views.disapprove_comment,name='remove_comment'),
   path('sendmail/<post_id>',views.Send_mail,name="send_mail"),
   path('feed/',LatestPostFeed(),name='post_feed'),
   # password change paths
   path('login/',views.UserLogin,name='login'),
   path('logout/',views.UserLogout,name='logout'),
   path('register/',views.UserRegistration,name='register'),
  
  
   
 

]
