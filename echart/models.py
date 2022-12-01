from django.db import models

# Create your models here.
class Market(models.Model):
    shareCode = models.CharField(max_length=10, verbose_name='shareCode')
    date = models.DateField(verbose_name='Date')
    openingPrice = models.FloatField(verbose_name='openingPrice')
    highestPrice = models.FloatField(verbose_name='highestPrice')
    lowestPrice = models.FloatField(verbose_name='lowestPrice')
    closingPrice = models.FloatField(verbose_name='closingPrice')
    priceDifferent = models.FloatField(verbose_name='priceDifferent')
    PriceDifferentPercentage= models.FloatField(verbose_name='PriceDifferentPercentage')
    TradingVolume= models.FloatField(verbose_name='TradingVolume')
    Amount= models.FloatField(verbose_name='Amount')
    StockAmplitude= models.FloatField(verbose_name='StockAmplitude')
    TurnoverRate= models.FloatField(verbose_name='TurnoverRate')

#class marketValue(models.Model):
#    shareCode = models.CharField(max_length=10, verbose_name='shareCode', primary_key=True)
#    value = models.FloatField(verbose_name='value(100 million)', default=0)


class stock(models.Model):
    shareCode = models.CharField(max_length=10, verbose_name='shareCode',primary_key=True)
    name = models.CharField(max_length=10, verbose_name='name')
    area = models.CharField(max_length=10, verbose_name='area', null=True)
    industry = models.CharField(max_length=10, verbose_name='industry', null=True)
    market = models.CharField(max_length=10, verbose_name='market', null=True)
    listDate = models.CharField(max_length=10, verbose_name='listDate')
    value = models.FloatField(verbose_name='value(100 million)', default=0)