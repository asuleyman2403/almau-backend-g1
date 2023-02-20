from online_shop.models import Category, Product
from online_shop.serializers import CategorySerializer, ProductSerializer, ProductModelSerializer
from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import Response
from rest_framework import status
from .utils import get_category, get_product


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
@renderer_classes([JSONRenderer])
def categories_handler(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        category = request.data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'message': 'Response is not supported'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_handler(request, pk):
    result = get_category(pk)

    if result['status'] == 404:
        return Response(data={'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    category = result['category']

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        category.delete()
        return Response(data={'message': 'Category deleted successfully!'}, status=status.HTTP_200_OK)

    return Response(data={'message': 'Response is not supported'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def category_products_handler(request, pk):
    result = get_category(pk)

    if result['status'] == 404:
        return Response(data={'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    category = result['category']

    if request.method == 'GET':
        products = category.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        product = request.data
        product['category_id'] = pk
        serializer = ProductSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'message': 'Response is not supported'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def product_handlers(request, pk):
    result = get_product(pk)

    if result['status'] == 404:
        return Response(data={'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    product = result['product']

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        product.delete()
        return Response(data={'message': 'Product deleted successfully!'}, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ProductSerializer(data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    return Response(data={'message': 'Response is not supported'}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def product_second_handlers(request, pk):
    result = get_product(pk)

    if result['status'] == 404:
        return Response(data={'message': 'Product not found'}, status=404)

    product = result['product']

    if request.method == 'GET':
        serializer = ProductModelSerializer(product)
        return Response(data=serializer.data, status=200)

    if request.method == 'DELETE':
        product.delete()
        return Response(data={'message': 'Product deleted successfully!'}, status=200)

    if request.method == 'PUT':
        serializer = ProductModelSerializer(data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    return Response(data={'message': 'Response is not supported'}, status=400)
