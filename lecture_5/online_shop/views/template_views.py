from django.shortcuts import render
from lecture_5.settings import STATIC_URL
from online_shop.models import Category, Product


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'online_shop/index.html', {'STATIC_URL': STATIC_URL, 'categories': categories})


def category_page(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, 'online_shop/category.html', {'category': category})




