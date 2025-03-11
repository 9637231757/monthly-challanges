from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dict = {
    "january":"Be vegetarian for a month",
    "february":"learn django for 20 minutes everyday",
    "march":"do excercises for 1 hour everyday",
    "april":"Be vegetarian for a month",
    "may":"learn django for 20 minutes everyday",
    "june":"do excercises for 1 hour everyday",
    "july":"Be vegetarian for a month",
    "august":"learn django for 20 minutes everyday",
    "september":"do excercises for 1 hour everyday",
    "november":"Be vegetarian for a month",
    "december":None
}
# Create your views here.

def index(request):
    months = list(monthly_challenges_dict.keys())
    
    return render(request,"challenges/index.html",{
        "months":months
    })
    
        

def monthly_challenges_dr(request, month):
    months = list(monthly_challenges_dict.keys())
    
    if month> len(months):
        return HttpResponseNotFound('invalid month')
       
    redirect_month = months[month -1]
    redirect_path = reverse('month_challenge', args=[redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path)
    

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name":month.capitalize()
        
        })
    except KeyError:
        return HttpResponseNotFound('this month is not supported')
        
    
 
    

