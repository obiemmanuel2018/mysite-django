from django.db import models
from django.core.mail import send_mail

# Create your models here.
class Project(models.Model):
      category=[
        ('Web','Web Develoment'),
        ('Mobile','Mobile Apps')
      ]
      name = models.CharField(max_length=200)
      image = models.ImageField(upload_to='projects/',null=False,blank=False)
      url = models.URLField()
      category = models.CharField(max_length=200,choices=category)


      def __str__(self):
            return self.name

      def save(self,*args,**kwargs):
           subject = 'Emmanuel\'s Portfolio'
           message = 'A new Project with the name @{} has been launched. Please do check it out at {}'.format(self.name,self.url)
           subscribers = Subscriber.objects.all()
           for i in range(len(subscribers)):
                 try:
                   send_mail(subject,message,'obiemmanuel2018@gmail.com',[subscribers[i].email],fail_silently=False)
                 except:
                   print('they was an error sending mail')
           return super().save(*args,**kwargs)
            
                 
              


class Client(models.Model):
      name = models.CharField(max_length=200)
      image = models.ImageField(upload_to='clients/%d/%m/%y',null=False)
      feed_back = models.TextField()

      def __str__(self):
            return str(self.name)
      




class Subscriber(models.Model):
      email = models.EmailField(blank=False,null=False)

      def __str__(self):
            return self.email

class Hire(models.Model):
      company_name=models.CharField(max_length=200,blank=True,null=True)
      email= models.EmailField()
      address = models.CharField(max_length=200)
      contact = models.IntegerField()
      city = models.CharField(max_length=200)
      job = models.CharField(max_length=200)
     


      def __str__(self):
            if self.company_name:
                  return self.company_name
            else:
                  return self.email + ' ' + str(self.address) + ' ' + self.job