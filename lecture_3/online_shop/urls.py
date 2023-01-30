
from django.urls import path
from online_shop import views

urlpatterns = [
    path('categories', views.get_categories),
    path('categories/<int:pk>', views.get_category),
    path('categories/<int:pk>/products', views.get_category_products),
    path('products', views.get_products),
    path('products/<int:pk>', views.get_product),
    path('categories/<int:pk1>/products/<int:pk2>', views.get_product_of_category)
]


