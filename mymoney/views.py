from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.


def read(request, pk):
    income = models.Income.objects.get(id=pk)
    context = {'income': income}
    return render(request, 'mymoney/list.html', context)


def index(request):
    return render(request, 'mymoney/list.html')
