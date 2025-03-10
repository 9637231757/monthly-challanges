from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

def monthly_challenges(request, month):
    nexttext = None
    if month == 'january':
        nextext = 'Be vegeterial for a month'
    elif month == 'february':
        nextext ='learn django for minutes everyday '
    elif month == 'march':
        nextext = 'excercise everyday for 1 hour '
    else:
        return HttpResponseNotFound('This month does not exit:') 
    return HttpResponse(nextext)           
                    