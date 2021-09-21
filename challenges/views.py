from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

challenges = {
    "january": "A",
    "february": "B",
    "march": "C",
    "april": "D",
    "may": "E",
    "june": "F",
    "july": "G",
    "august": "H",
    "september": "I",
    "october": "J",
    "november": "K",
    "december": "L",
}

def home(request):
    html = ""
    months = list(challenges.keys())

    for month in months:
        html += f'<li><a href="{month}">{month.capitalize()}</a></li>'

    return HttpResponse(f'<ul>{html}</ul>')

def index_by_int(request, month):
    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid month")

    monthName = list(challenges.keys())[month - 1]
    return HttpResponseRedirect(monthName)

def index(request, month):
    try:
        return HttpResponse(challenges[month])
    except:
        return HttpResponseNotFound("Not found")