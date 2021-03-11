from django.core.management.base import BaseCommand, CommandError
from infoProduct.models import ProductQuantity
import requests
import time

from infoProduct.management.commands.updateSale import updateSale


class updateQty(BaseCommand):

    def add(id, qty):
        product = ProductQuantity.objects.get(tigID=id)
        product.quantity += qty
        product.save()
        if (product.quantity <= 16):
            updateSale.remove(product.tigID)
        elif (16 < product.quantity < 64):
            updateSale.update(product.tigID, 50.0)
        else:
            updateSale.update(product.tigID, 80.0)

    def remove(id, qty):
        product = ProductQuantity.objects.get(tigID=id)
        if (product.quantity - qty > 0):
            product.quantity -= qty
        else:
            product.quantity = 0
        product.save()
        if (product.quantity <= 16):
            updateSale.remove(product.tigID)
        elif (16 < product.quantity < 64):
            updateSale.update(product.tigID, 50.0)
        else:
            updateSale.update(product.tigID, 80.0)
