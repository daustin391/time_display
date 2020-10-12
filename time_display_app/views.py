from django.shortcuts import render, HttpResponse
from datetime import datetime


def time_display(request):
    context = {
        "date": datetime.now().strftime("%b %-d, %Y"),
        "time": datetime.now().strftime("%-I:%M %p"),
    }
    return render(request, "index.html", context)
