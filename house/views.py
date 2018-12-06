from django.shortcuts import render
from django.http import HttpResponse
from house.models import House
# Create your views here.
def index(request):
    shuju = House.objects.get(pk=1011)
    print(shuju.name, shuju.price, shuju.url)
    return HttpResponse('hello world')