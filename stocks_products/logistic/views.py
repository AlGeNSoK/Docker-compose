from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class CustomSearchFilter(SearchFilter):
    search_param = 'products'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, OrderingFilter, CustomSearchFilter]
    search_fields = ['products__id', 'products__title', 'products__description']
