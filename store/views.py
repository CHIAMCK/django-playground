from django.shortcuts import render
from .models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])
# takes a list of HTTP methods that your view should respond to
def view_books(request):

    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_201_CREATED)
