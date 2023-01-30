from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from online_shop.models import Category, Product


def get_categories(request):
    categories = Category.objects.all()
    categories_list = [category.to_json() for category in categories]

    return JsonResponse(categories_list, status=200, safe=False)


def get_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': 'Category does not exist'}, status=404)

    return JsonResponse(category.to_json(), status=200)


def get_products(request):
    products = Product.objects.all()
    products_list = [product.to_json() for product in products]

    return JsonResponse(products_list, status=200, safe=False)


def get_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': 'Product does not exist'}, status=404)

    return JsonResponse(product.to_json(), status=200)


def get_category_products(request, pk):
    try:
        category = Category.objects.get(id=pk)
        products = category.product_set.all()
        products_list = [product.to_json() for product in products]
        return JsonResponse(products_list, status=200, safe=False)

    except Category.DoesNotExist as e:
        return JsonResponse({'message': 'Category does not exist'}, status=404)


def get_product_of_category(request, pk1, pk2):
    try:
        category = Category.objects.get(id=pk1)
        try:
            product = category.product_set.get(id=pk2)
        except Product.DoesNotExist as e:
            return JsonResponse({'message': 'Category does not have such product'}, status=404)
        return JsonResponse(product.to_json(), status=200, safe=False)

    except Category.DoesNotExist as e:
        return JsonResponse({'message': 'Category does not exist'}, status=404)
