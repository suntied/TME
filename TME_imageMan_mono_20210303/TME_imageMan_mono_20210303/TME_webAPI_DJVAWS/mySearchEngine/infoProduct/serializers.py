from rest_framework.serializers import ModelSerializer
from infoProduct.models import ProductQuantity, ProductSale


class InfoProductSerializer(ModelSerializer):
    class Meta:
        model = ProductQuantity
        fields = ('quantity', 'tigID')


class SaleInfoSerializer(ModelSerializer):
    class Meta:
        model = ProductSale
        fields = ('discount', 'tigID')
