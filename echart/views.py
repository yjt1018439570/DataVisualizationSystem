from django.db.models import Sum, Count
from django.http import HttpResponse
from django.shortcuts import render
from echart.models import Market, stock

from django.core import serializers


# Create your views here.
def echarts(request):
    totalIndustry = (stock.objects
                     .values('industry')
                     .annotate(total=Sum('value'))
                     .order_by('-total')
                     )[:10]

    topTen = (stock.objects
              .values('name', 'value')
              .order_by('-value')
              )[:10]

    byArea = (stock.objects
              .values('area')
              .order_by('area')
              .annotate(count=Count('name')))

    #for i in byArea:
        #print(i)
    return render(request, 'index.html', locals())

def search(request, id):
    info=stock.objects.filter(shareCode=id)
    totalIndustry = (stock.objects
                     .values('industry')
                     .annotate(total=Sum('value'))
                     .order_by('-total')
                     )[:10]

    topTen = (stock.objects
              .values('name', 'value')
              .order_by('-value')
              )[:10]

    byArea = (stock.objects
              .values('area')
              .order_by('area')
              .annotate(count=Count('name')))

    id = Market.objects.filter(shareCode=id)
    return render(request, 'index.html', locals())



