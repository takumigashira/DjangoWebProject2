from email import message
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloMyApp/index.html",
            {
                'title': "Hello MyApp",
                'message': "Hello Django!",
                'content': " on " + now.strftime("%A, %d %B, %Y at %X")
            }
        )