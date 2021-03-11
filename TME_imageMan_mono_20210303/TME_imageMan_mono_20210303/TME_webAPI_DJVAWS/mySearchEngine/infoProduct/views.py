import requests
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from infoProduct.models import ProductQuantity, ProductSale
from infoProduct.serializers import InfoProductSerializer, SaleInfoSerializer
from infoProduct.Utils import Utils

# Create your views here.
from infoProduct.management.commands.updateQty import updateQty
from infoProduct.management.commands.updateSale import updateSale


class InfoProduct(APIView):

    def get(self, request, id, format=None):
        product = Utils.get_object_quantity(id)
        jsondata = None
        if product:
            serializer = InfoProductSerializer(product)

            response = requests.get(baseUrl + 'product/' + str(id) + '/')
            jsondata = response.json()
            jsondata['quantityInStock'] = serializer.data['quantity']
        return Response(jsondata)


class InfoProducts(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl + 'products/')
        data = response.json()
        listResponse = list()
        for productList in data:
            product = Utils.get_object_quantity(productList['id'])
            if product:
                serializer = InfoProductSerializer(product)
                productList["quantity"] = serializer.data['quantity']
            listResponse.append(productList)
        return Response(listResponse)


class IncrementQuantity(APIView):
    def get(self, request, id, qty):
        updateQty.add(id, qty)
        data = Utils.manage_quantity(id)
        return Response(data)


class DecrementQuantity(APIView):
    def get(self, request, id, qty):
        updateQty.remove(id, qty)
        data = Utils.manage_quantity(id)
        return Response(data)


class SetSale(APIView):

    def get(self, request, id, newprice, format=None):
        prod = Utils.get_object_sale(id)
        jsondata = None
        if prod:
            prod.discount = float(newprice)
            prod.save()
            serializer = SaleInfoSerializer(prod)
            response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
            jsondata = response.json()
            if prod.discount > 0.0:
                jsondata["discount"] = prod.discount
                jsondata["sale"] = True
            else:
                jsondata["discount"] = prod.discount
                jsondata["sale"] = False
        return Response(jsondata)


class RemoveSale(APIView):
    def get(self, request, id, format=None):
        product = Utils.get_object_sale(id)
        jsondata = None
        if product:
            product.discount = 0.0
            product.save()
            serializer = SaleInfoSerializer(product)
            response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
            jsondata = response.json()
            if product.discount > 0.0:
                jsondata["discount"] = product.discount
                jsondata["sale"] = True
            else:
                jsondata["discount"] = product.discount
                jsondata["sale"] = False
        return Response(jsondata)
