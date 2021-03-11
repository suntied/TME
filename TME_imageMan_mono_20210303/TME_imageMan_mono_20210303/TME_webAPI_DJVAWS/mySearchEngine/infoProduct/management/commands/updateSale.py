from django.core.management.base import BaseCommand, CommandError
from infoProduct.models import ProductSale


class updateSale(BaseCommand):

    def update(id, price):
        product = ProductSale.objects.get(tigID=id)
        product.discount = price
        product.save()

    def remove(id):
        product = ProductSale.objects.get(tigID=id)
        product.discount = 0.0
        product.save()
