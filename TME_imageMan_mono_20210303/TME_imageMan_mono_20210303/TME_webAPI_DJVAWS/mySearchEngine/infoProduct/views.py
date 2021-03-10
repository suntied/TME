import requests
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from infoProduct.models import ProductQuantity
from infoProduct.serializers import InfoProductSerializer


# Create your views here.

class InfoProduct(APIView):

    def get_object_quantity(self, id):
        try:
            prod = ProductQuantity.objects.get(tigID=id)
            serializer = InfoProductSerializer(prod)
            return serializer.data['quantity']
        except ProductQuantity.DoesNotExist:
            return 0

    def get_object_sale(self, id):
        try:
            prod = ProductQuantity.objects.get(tigID=id)
            return prod
        except ProductQuantity.DoesNotExist:
            return False

    def get(self, request, id, format=None):
        response = requests.get(baseUrl + 'product/' + str(id) + '/')
        jsondata = response.json()
        jsondata['quantityInStock'] = self.get_object_quantity(id)
        isOnSale = self.get_object_sale(id)
        if isOnSale:
            jsondata['sale'] = isOnSale.sale
            jsondata['discount'] = isOnSale.discount
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"
class InfoProducts(APIView):
    def get_object(self, id):
        try:
            return ProductQuantity.objects.get(tigID=id)
        except ProductQuantity.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        response = requests.get(baseUrl + 'products/')
        jsondata = response.json()
        jsonResponse = []
        for prod in jsondata:
            prodSer = self.get_object(prod['id'])
            serializer = InfoProductSerializer(prodSer)
            prod["quantity"] = serializer.data['quantity']
            jsonResponse.append(prod)
        # Add serializer here
        return Response(jsonResponse)