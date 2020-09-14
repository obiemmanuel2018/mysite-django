from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment,UserProfileInfo
from blog.forms import PostForm,PostUpdateForm,CommentForm,UserForm,ProfileForm,MailForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http  import require_POST
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.forms.models import model_to_dict
from django.core.mail import send_mail
from django.db.models import Count
import pickle
import os
import re
import json 


def get_next_url(next):
    # check if url has next...then get the next page to navigate too after login
    if next:
       next = next.split('/')
       if 'blog:post_detail' in next:
           return next
       elif 'password_change' in next:
             return next
    else:
        return None 



def UserRegistration(request):
    # check if url has next...then get the next page to navigate too after login
    if 'next' in request.GET:
           next=request.GET.get('next')
           navigate_to = get_next_url(next)

           #############################################
    else:
        navigate_to=None

    if request.method=="POST":
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST)
   
        if userform.is_valid() and profileform.is_valid():
           user = userform.save()
           user.set_password(user.password)
           user.save()
           profile = profileform.save(commit=False)
           profile.user = user

           if 'profile_pic' in request.FILES:
               profile.profile_pic = request.FILES['profile_pic']
           profile.save()
           user = authenticate(username=userform.cleaned_data['username'],password=userform.cleaned_data['password'])
           login(request,user)
           print(navigate_to)
           if navigate_to:
                   if 'blog:post_detail' in navigate_to:
                       return HttpResponseRedirect(reverse('blog:post_detail',args=[navigate_to[1]]))
                   elif 'password_change' in navigate_to:
                        return HttpResponseRedirect(reverse('password_change'))
           else:
                return HttpResponseRedirect(reverse('blog:post_list'))
           
    else:
        userform = UserForm()
        profileform = ProfileForm()
    return render(request,'registration/register.html',{'userform':userform,'profileform':profileform})

    

def UserLogin(request):

    
    if 'next' in request.GET:
           next=request.GET.get('next')
           navigate_to = get_next_url(next)

    else:
        navigate_to = None

    
    ##################################
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                # if u have a url then navigate to post details page else to post list page
                if navigate_to:
                   if 'blog:post_detail' in navigate_to:
                       return HttpResponseRedirect(reverse('blog:post_detail',args=[navigate_to[1]]))
                   elif 'password_change' in navigate_to:
                        return HttpResponseRedirect(reverse('password_change'))
                   
                else:
                    return HttpResponseRedirect(reverse('blog:post_list'))
            else:
                return HttpResponse('User is in active')
        else: 
            return render(request,'registration/login.html',{'Error':'Invalid Credintials'})

    else:
        return render(request,'registration/login.html')


@login_required
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:login'))


def Post_list(request):
    if request.POST.get('query'):
       query =  request.POST.get('query')
       searched_post = Post.objects.filter(title__contains=query)[:10]
       context1={}
       clean = re.compile('<.*?>')
       for post in searched_post:
           i = 0
           post.title = re.sub(clean,'',post.title)
           context1[i] = [post.title,post.id] 
           i = i + 1 
       return JsonResponse(context1) 
       
    all_posts = Post.objects.filter(status='published').order_by('-published_date')
    trending_posts = Post.objects.all().annotate(num_comments=Count('comments')).order_by('-num_comments')[:20]
    
    # pagination for all_post
    paginator = Paginator(all_posts, 4) # 3 posts in each page
    page = request.GET.get('page')
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        all_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        all_posts = paginator.page(paginator.num_pages)

    drafts = Post.objects.filter(status='draft').order_by('-created_date')
    return render(request,'blog/posts/post_list.html',{'all_posts':all_posts,'trending_posts':trending_posts,'drafts':drafts,'page':page})



def Post_detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.user.is_anonymous:
        print('Anonymous User')
    else:
        post.views.add(request.user)
   
    ########################################
    # Adding views to post##################
    ########################################
   
    #########################################
    if(request.method == 'POST'):
        user_id = request.POST.get('number')
        user=get_object_or_404(User,id=user_id)
        user_profile_obj = UserProfileInfo.objects.filter(user=user_id)[0]
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.post = post
            comment_form.author = user.username    
            
            if user_profile_obj:
                comment_form.author_profile_pic=user_profile_obj.profile_pic
               
            else:
                 comment_form.author_profile_pic='profile_pics/default_profile.jpg'
            
               
            comment_form.save()
            if not request.user.is_superuser:
               url = request.build_absolute_uri(post.get_absolute_url())
               subject='From Blog:'
               message='Hello Sir, {} just added a comment on {}.follow link to delete or approve comment {}.'.format(request.user,post.title,url)
               send_mail(subject,message,request.user.email,['obiemmanuel2018@gmail.com'],fail_silently=False)
               messages.info(request,'Thanks {} for commenting. Your comment needs to be approved by admin before added to post'.format(user.username))
            return JsonResponse({'comment':{'id':comment_form.id,'author':comment_form.author,'body':comment_form.body,'author_profile_pic':str(comment_form.author_profile_pic),'created_date':comment_form.created_date}})
        else:
            print('Invalid form')
    else:
        comment_form = CommentForm()
    return render(request,'blog/posts/post_detail.html',{'post':post,'comment_form':comment_form})

@login_required
def Post_delete(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse_lazy('blog:post_list'))



@login_required
def Post_create(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            
            form = form.save(commit=False)
            user = get_object_or_404(User,username=request.user)
            form.author=user
            print(user)
            form.status = 'draft'
            form.save()
            return HttpResponseRedirect(reverse('blog:post_list'))
        else:
            print('Form is Invalid')
    else:
        form = PostForm()
    return render(request,'blog/posts/post_create.html',{'form':form})

@login_required
def Post_update(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method =='POST':
        form = PostUpdateForm(request.POST)
        if form.is_valid():

            cd = form.cleaned_data
            if not  cd['title']:
                post.title = post.title
            else:
                post.title = cd['title']
            if not cd['body']:
                post.body = post.body
            else:
                post.body = cd['body']

            post.save()
            return HttpResponseRedirect(reverse('blog:post_detail',args=[post_id]))
        else:
            print('Form is Invalid')
    else:
        form = PostUpdateForm(initial={'title':post.title,'body':post.body})
    return render(request,'blog/posts/post_update.html',{'form':form,'post':post})





@login_required
def Draft_publish(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    post.publish()
    drafts=Post.objects.filter(status='draft')
    total_drafts = drafts.count()
    return JsonResponse({'status':'OK','total_drafts':total_drafts})

@login_required
def Draft_delete(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    
    post.delete()
    drafts=Post.objects.filter(status='draft')
    total_drafts = drafts.count()
    return JsonResponse({'status':'OK','total_drafts':total_drafts})







################################################################################
################################################################################


@login_required
def approve_comment(request,comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    comment.approve()
    return JsonResponse({'status':'comment approved succesfully'})

@login_required
def disapprove_comment(request,comment_id):
     comment = get_object_or_404(Comment,id=comment_id)
     comment.delete()
     return JsonResponse({'status':'comment deleted succesfully'})

    



########################################################
########################################################
def Send_mail(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='published')

    Success = False
    Failure = False
    if request.method =='POST':
        mail_form = MailForm(request.POST)
        if mail_form.is_valid():
            cd = mail_form.cleaned_data
            print(cd)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} recommends you read {}'.format(cd['name'],post.title)
            message = 'Read {} at {}\n\n {}\'s comments:{}'.format(post.title,post_url,cd['name'],cd['comment'])
            try:
               send_mail(subject,message,'obiemmanuel2018@gmail.com',[cd['to']],fail_silently=False)
               Success = True
            except:
                Failure = True 
                Success = False
    else:
        mail_form = MailForm()
    return render(request,'share/gmail_form.html',{'mailform':mail_form,'success':Success,'failure':Failure})





