from django.urls import path
from online_shop import views

urlpatterns = [
    path('', views.index_page),
    path('categories/<int:pk>', views.category_page),
    path('api/categories', views.categories_handler),
    path('api/categories/<int:pk>', views.category_handler),
    path('api/categories/<int:pk>/products', views.category_products_handler),
    # path('products/<int:pk>', views.product_handlers),
    path('api/products/<int:pk>', views.product_second_handlers),
]
