from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from online_shop.models import Category, Product
from online_shop.serializers import CategorySerializer, ProductSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def categories_handler(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data)
        categories = Category.objects.all()

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)


def get_category(pk):
    try:
        category = Category.objects.get(id=pk)
        return {
            'category': category,
            'status': 200
        }
    except Category.DoesNotExist as e:
        return {
            'category': None,
            'status': 404
        }

def get_product(pk):
    try:
        product = Product.objects.get(id=pk)
        return {
            'product': product,
            'status': 200
        }
    except Product.DoesNotExist as e:
        return {
            'product': None,
            'status': 404
        }

@csrf_exempt
def category_handler(request, pk):
    result = get_category(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Category not found'}, status=404)

    category = result['category']

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data, instance=category)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, 400)
    if request.method == 'DELETE':
        category = Category.objects.get(id=pk)
        category.delete()
        serializer = CategorySerializer(category)
        return JsonResponse({'message': 'Category successfully deleted'}, status=200)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)


@csrf_exempt
def category_products_handler(request, pk):
    result = get_category(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Category not found'}, status=404)

    category = result['category']

    if request.method == 'GET':
        products = category.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        data['category_id'] = pk
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)


@csrf_exempt
def product_handler(request, pk):
    result = get_product(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Product not found'}, status=404)

    product = result['product']

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = ProductSerializer(data=data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product was successfully deleted'}, status=200)

    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)
