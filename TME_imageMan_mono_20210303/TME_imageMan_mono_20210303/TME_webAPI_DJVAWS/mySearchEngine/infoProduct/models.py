from django.db import models


# Create your models here.

class ProductQuantity(models.Model):
    tigID = models.IntegerField(default='-2')
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ('tigID',)


class ProductSale(models.Model):
    discount = models.FloatField(default=0.0)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('discount', 'tigID')
