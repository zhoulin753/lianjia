from django.shortcuts import render
from django.http import HttpResponse
from house.models import House
# Create your views here.
def index(request):
    shuju = House.objects.all()
    print(shuju)
    return HttpResponse('hello world')