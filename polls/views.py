from django.shortcuts import render
from django.http import HttpResponse

# Create your views from django.http import HttpsResponse

def index(request):
	return HttpResponse("Hello, world!")
