from django.shortcuts import render

# Create your views here.
from django.forms.models import model_to_dict
import json
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.serializers import ProductSerializer

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        # data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
    return Response(data)