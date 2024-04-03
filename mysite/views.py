from django.http import HttpResponse
from django.shortcuts import render

def home(response):
  return HttpResponse("This is Home")