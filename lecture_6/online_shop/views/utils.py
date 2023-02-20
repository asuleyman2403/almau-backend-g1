from online_shop.models import Category, Product

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