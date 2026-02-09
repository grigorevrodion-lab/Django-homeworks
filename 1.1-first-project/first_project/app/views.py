from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import os


def home_view(request):
    pages = [
        {'name': 'Текущее время', 'url': '/current_time/'},
        {'name': 'Рабочая директория', 'url': '/workdir/'},
    ]
    return render(request, 'home.html', {'pages': pages})


def current_time_view(request):
    now = datetime.now()
    return HttpResponse(f'Текущее время: {now}')


def workdir_view(request):
    files = os.listdir('.')
    return HttpResponse('<br>'.join(files))
