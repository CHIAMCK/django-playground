from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET'])
# takes a list of HTTP methods that your view should respond to
def view_books(request):
    if 'product' in cache:
        products = cache.get('product')
        return Response(products, status=status.HTTP_201_CREATED)

    else:
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        print(results)
        cache.set('product', results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)
