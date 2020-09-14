from django import forms
from .models import Subscriber,Hire


class SubscriberForm(forms.ModelForm):
      class Meta:
            model = Subscriber
            fields=('email',)

class HireForm(forms.ModelForm):
      class Meta:
            model = Hire
            fields=('company_name','email','address','contact','city','job')



