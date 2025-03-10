from django.urls import path
from . import views

urlpatterns = [
    
        path('<str:month>/', views.monthly_challenges, name='months'),  
        path('<int:month>/', views.monthly_challenges_dr, name='months_dr'),    
  


]
