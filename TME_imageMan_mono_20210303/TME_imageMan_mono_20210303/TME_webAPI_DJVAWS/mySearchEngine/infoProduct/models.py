from django.db import models


# Create your models here.

class ProductQuantity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-2')
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ('tigID',)
