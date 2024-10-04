from django.shortcuts import render
from django.http import HttpResponse
import random


def test_view(request):
    return render(request, 'base.html')
