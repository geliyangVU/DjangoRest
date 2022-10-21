import imp
from pickletools import read_long4
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

# multiple serializer can be implemented and called to provide more flexible data models:
# here is an example of a secondary serializer
# class SecondaryProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     class Meta :
#         model = Product
#         fields = [
#             'title',
#             'content',
#             'price',
#             'sale_price',
#         ]

#     def get_my_discount(self, obj):
#         return obj.get_discount()
