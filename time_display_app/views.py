from django.shortcuts import render, HttpResponse
from datetime import datetime


def time_display(request):
    context = {"time": datetime.now().strftime("%d/%m/%Y")}
    return render(request, "index.html", context)
