from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return HttpResponse("Wow this is an <strong>awesome</strong> Django 2020")
# Create your views here.
