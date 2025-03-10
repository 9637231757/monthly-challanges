from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

monthly_challenges_dict = {
    "january":"Be vegeterial for a month",
    "feburary":"learn django for 20 minutes everyday",
    "march":"do excercies for 1 hour everyday",
    "april":"Be vegeterial for a month",
    "may":"learn django for 20 minutes everyday",
    "june":"do excercies for 1 hour everyday",
    "july":"Be vegeterial for a month",
    "august":"learn django for 20 minutes everyday",
    "september":"do excercies for 1 hour everyday",
    "november":"Be vegeterial for a month",
    "december":"do excercies for 1 hour everyday"
}
# Create your views here.

def monthly_challenges_dr(request, month):
    months = list(monthly_challenges_dict.keys())
    
    if month> len(months):
        return HttpResponseNotFound('invalid month')
    
    redirect_month = months[month -1]
    return HttpResponseRedirect("/challenges/"+ redirect_month)
    

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound('this month is not supported')
    
    

