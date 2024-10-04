from django.shortcuts import render
from django.http import HttpResponse
import random


def random_number(request):
    return HttpResponse(random.randint(1, 100))


def test_view(request):
    return render(request, 'base.html')


