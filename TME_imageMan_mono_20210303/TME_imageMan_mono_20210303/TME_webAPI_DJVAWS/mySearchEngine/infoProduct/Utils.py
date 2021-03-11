import requests
from infoProduct.models import ProductSale
from infoProduct.models import ProductQuantity
from mytig.config import baseUrl
from infoProduct.serializers import InfoProductSerializer


class Utils:
    @staticmethod
    def get_object_quantity(id):
        try:
            return ProductQuantity.objects.get(tigID=id)
        except ProductQuantity.DoesNotExist:
            return False

    @staticmethod
    def get_object_sale(id):
        try:
            return ProductSale.objects.get(tigID=id)
        except ProductSale.DoesNotExist:
            return False

    @staticmethod
    def manage_quantity(id):
        prodSer = Utils.get_object_quantity(id)
        data = None
        if prodSer:
            serializer = InfoProductSerializer(prodSer)
            response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
            data = response.json()
            data["quantity"] = serializer.data['quantity']
            prod = ProductSale.objects.get(tigID=id)
            data['discount'] = prod.discount
            if prod.discount != 0.0:
                data['sale'] = True
            else:
                data['sale'] = False
        return data
