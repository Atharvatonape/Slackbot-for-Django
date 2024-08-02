from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def slack_events_endpoint(request):
    return HttpResponse("<h1> Hello World </h1>")