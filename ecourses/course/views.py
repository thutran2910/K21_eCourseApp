from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def index(request):
    return HttpResponse("Hello  e-Course App")
# Create your views here.

def welcome(request,year):
    return HttpResponse("HELLO" + str(year))

class TestView(View):
    def get(self, request):
        return HttpResponse("TESTING")

    def post(self, request):
        pass