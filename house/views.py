from django.shortcuts import render
from django.http import HttpResponse
from house.models import House


def info_context(shuju):
    context = {}
    num = House.objects.count()
    page = num / 30
    if page > int(page):
        page = int(page) + 1
    else:
        page = int(page)
    context['shuju'] = shuju
    context['page'] = page
    return context


def index(request):
    shuju = House.objects.filter(pk__lte=30)
    context = info_context(shuju)
    return render(request, 'index.html', context=context)


def get_page(request, page):
    house_id = int(page) * 30 - 29
    shuju = House.objects.filter(pk__lte=int(page) * 30, pk__gte=house_id)
    context = info_context(shuju)
    return render(request, 'index.html', context=context)

