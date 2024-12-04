from django.shortcuts import render , HttpResponse


def index(request):
  return HttpResponse('Hi index ')

# Create your views here.
