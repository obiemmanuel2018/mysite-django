from django import forms
from blog.models import Post,Comment,UserProfileInfo
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
      password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'Input','placeholder':'Password'}))
      confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'Input','placeholder':'Confirm Password'}))
      class Meta:
          model=User
          fields =('first_name','username','email','password','confirm_password')
          help_texts = {
            'username': None,
            'password': None,
            'first_name':None
        }
          widgets = {
              'username':forms.TextInput(attrs={'class':'Input','placeholder':'Username'}),
              'email':forms.TextInput(attrs={'class':'Input','placeholder':'Email'}),
              'first_name':forms.TextInput(attrs={'class':'Input','placeholder':'First Name'}),
              
                    }
     
      def clean_confirm_password(self):
          password = self.cleaned_data['password']
         
          confirm_password = self.cleaned_data['confirm_password']
         
          if len(password)<8:
             raise ValidationError('Password should be atleast 8 characters long')
             return password
          elif password !=confirm_password:
              raise ValidationError('Password and Confirm password doesn\'t match')
          return confirm_password


class ProfileForm(forms.ModelForm):
       class Meta:
           model = UserProfileInfo
           fields =('profile_pic',)
          
           widgets ={
               'profile_pic':forms.FileInput(attrs={'class':'profileInput'})
           }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title','body','image')
       

        widgets = {
            # 'author':forms.TextInput(attrs={'disabled':False}),
            'title':forms.TextInput(attrs={'class':'post_title'}),
            'body':forms.Textarea(attrs={'class':'editable'}),
            'author':forms.HiddenInput
        }
       
class PostUpdateForm(forms.ModelForm):
      
      class Meta:
            model = Post
            fields = ('title','body')
            
            widgets={
                'body':forms.Textarea(attrs={'class':'editable'}),
                'title':forms.Textarea(attrs={'class':'editable'})
            }



class CommentForm(forms.ModelForm):
      class Meta():
            model = Comment
            fields = ('body',)

            widgets = {
           
            'body':forms.Textarea(attrs ={'class':'editable comment_form'})
             }
            labels ={
                 "body":""
             }
            
class MailForm(forms.Form):
      name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'Input','placeholder':'subject'}))
      email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'Input','placeholder':'from@gmail.com'}))
      to = forms.EmailField(widget=forms.TextInput(attrs={'class':'Input','placeholder':'to@gmail.com'}))
      comment = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'commentInput','placeholder':'message'}))



     
            