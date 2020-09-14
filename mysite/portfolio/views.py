from django.shortcuts import render
from .models import Subscriber,Project,Client
from django.http import JsonResponse
from portfolio.forms import SubscriberForm,HireForm
from django.views.decorators.http import require_POST
# Create your views here.

def home(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    return render(request,'portfolio/home.html',context={'projects':projects,'clients':clients})
def subscribe(request):
    if request.method=='POST':
       subscribers = Subscriber.objects.all()
       form = SubscriberForm(request.POST);
       if form.is_valid():
          email = request.POST.get('email')
          try:
             form = form.save(commit=False)
             if subscribers:
                 for i in range(len(subscribers)):
                    if email==subscribers[i].email:
                       return JsonResponse({'status':'You are a subscriber'})
             form.email = email
             form.save()
             return JsonResponse({'status':'Ok'})
          except:
              return JsonResponse({'status':'Error'})


@require_POST
def hire(request):
    if request.method =='POST':
       form = HireForm(request.POST)
       if form.is_valid():
          form = form.save(commit=False)
          form.email = request.POST.get('email')
          form.company_name = request.POST.get('company_name')
          form.address = request.POST.get('address')
          form.contact = request.POST.get('contact')
          form.city = request.POST.get('city')
          form.job = request.POST.get('job')

          form.save()
          
          return JsonResponse({'status':'OK'})
       else:
           return JsonResponse({'status':'form is invalid!'})

    else:
       return JsonResponse({'status':'Opps Something went wrong!'})
    
    
    

