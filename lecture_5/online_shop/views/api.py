from django.http import HttpResponse, JsonResponse
from online_shop.models import Category, Product
from online_shop.serializers import CategorySerializer, ProductSerializer, ProductModelSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
import json


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
def categories_handler(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)

    if request.method == 'POST':
        category = json.loads(request.body)
        serializer = CategorySerializer(data=category)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse(data={'message': 'Response is not supported'}, status=400)


@csrf_exempt
def category_handler(request, pk):
    result = get_category(pk)

    if result['status'] == 404:
        return JsonResponse(data={'message': 'Category not found'}, status=404)

    category = result['category']

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(data=serializer.data, status=200, safe=False)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'message': 'Invalid content'}, status=400)
        serializer = CategorySerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False)
        return JsonResponse(data=serializer.errors, status=404, safe=False)

    if request.method == 'DELETE':
        category.delete()
        return JsonResponse(data={'message': 'Category deleted successfully!'}, status=200, safe=False)

    return JsonResponse(data={'message': 'Response is not supported'}, status=400)


@csrf_exempt
def category_products_handler(request, pk):
    result = get_category(pk)

    if result['status'] == 404:
        return JsonResponse(data={'message': 'Category not found'}, status=404)

    category = result['category']

    if request.method == 'GET':
        products = category.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)

    if request.method == 'POST':
        product = json.loads(request.body)
        product['category_id'] = pk
        serializer = ProductSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse(data={'message': 'Response is not supported'}, status=400)

@csrf_exempt
def product_handlers(request, pk):
    result = get_product(pk)

    if result['status'] == 404:
        return JsonResponse(data={'message': 'Product not found'}, status=404)

    product = result['product']

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(data=serializer.data, status=200, safe=False)

    if request.method == 'DELETE':
        product.delete()
        return JsonResponse(data={'message': 'Product deleted successfully!'}, status=200, safe=False)

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = ProductSerializer(data=data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse(data={'message': 'Response is not supported'}, status=400)

@csrf_exempt
def product_second_handlers(request, pk):
    result = get_product(pk)

    if result['status'] == 404:
        return JsonResponse(data={'message': 'Product not found'}, status=404)

    product = result['product']

    if request.method == 'GET':
        serializer = ProductModelSerializer(product)
        return JsonResponse(data=serializer.data, status=200, safe=False)

    if request.method == 'DELETE':
        product.delete()
        return JsonResponse(data={'message': 'Product deleted successfully!'}, status=200, safe=False)

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = ProductModelSerializer(data=data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse(data={'message': 'Response is not supported'}, status=400)
