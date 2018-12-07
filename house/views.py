from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


from house.models import House
# Create your views here.
def index(request):
    shuju = House.objects.all()
    # print(shuju.name, shuju.price, shuju.url)
    context = {'shuju':shuju}
    temp = loader.get_template('index.html')
    return render(request, 'index.html' ,context=context)
    # return HttpResponse(temp.render(context))