from django.utils import timezone
from django.shortcuts import render
from datetime import datetime
import pytz


def time_display(request):

    context = {
        "date": timezone.now().strftime("%b %-d, %Y"),
        "time": timezone.now().strftime("%-I:%M %p"),
    }
    return render(request, "index.html", context)
