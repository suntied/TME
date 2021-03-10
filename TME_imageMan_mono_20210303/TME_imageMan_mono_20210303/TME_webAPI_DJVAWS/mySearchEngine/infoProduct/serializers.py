from rest_framework.serializers import ModelSerializer
from infoProduct.models import ProductQuantity


class InfoProductSerializer(ModelSerializer):
    class Meta:
        model = ProductQuantity
        fields = ('id','tigID','quantity')
