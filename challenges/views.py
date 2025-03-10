from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

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
    "december":"do excercises for 1 hour everyday"
}
# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month_challenge', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
        


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
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound('this month is not supported')
    
    

