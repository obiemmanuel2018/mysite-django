from django.urls import path
from . import views
app_name='portfolio'

urlpatterns = [
    path('',views.home,name='home'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('hire/',views.hire,name='hire')
]