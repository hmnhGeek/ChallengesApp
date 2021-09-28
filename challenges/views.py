from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

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
    "november": None,
    "december": "L",
}

def home(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {"months": months})

def index_by_int(request, month):
    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid month")

    monthName = list(challenges.keys())[month - 1]
    return HttpResponseRedirect(monthName)

def index(request, month):
    try:
        return render(request, "challenges/challenge.html", {"text": challenges[month], "month": month.capitalize()})
    except:
        return HttpResponseNotFound("Not found")