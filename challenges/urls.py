from django.urls import path
from . import views

urlpatterns = [
        
        path('<int:month>/', views.monthly_challenges_dr),    
        path('<str:month>/', views.monthly_challenges),  
  


]
