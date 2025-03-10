from django.urls import path
from . import views

urlpatterns = [
        
        path('<int:month>/', views.monthly_challenges_dr, name = 'months'),    
        path('<str:month>/', views.monthly_challenges, name = 'month_challenge'),  
  


]
