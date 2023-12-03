from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
monthly_challenges = {
    "january": "eat no meat for the entire month",
    "february": "walk at least 20 minutes everyday",
    "march": "learn django 20 minutes everyday",
    "april": "eat no meat for the entire month",
    "may": "walk at least 20 minutes everyday",
    "june": "learn django 20 minutes everyday",
    "july": "eat no meat for the entire month",
    "august": "walk at least 20 minutes everyday",
    "september": "learn django 20 minutes everyday",
    "october": "eat no meat for the entire month",
    "november": "walk at least 20 minutes everyday",
    "december": "learn django 20 minutes everyday",
}
# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported")
