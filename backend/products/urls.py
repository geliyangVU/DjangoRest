from http.client import ImproperConnectionState
from django.urls import path

from . import views

urlpatterns = [
    path('<>', views.ProductDetailAPIView.as_view())
]

