from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def book_tabl(request):
    return HttpResponse("Model BOOK")
