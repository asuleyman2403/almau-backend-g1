from rest_framework import serializers
from online_shop.models import Category, Product


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, allow_null=False)
    description = serializers.CharField(min_length=10, max_length=1000, allow_null=True)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, allow_null=False)
    price = serializers.IntegerField(min_value=0, allow_null=False)
    code = serializers.CharField(allow_null=False)
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(required=False, read_only=True)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.code = validated_data.get('description', instance.code)
        instance.category_id = validated_data.get('category_id', instance.category_id)

        instance.save()
        return instance


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = '__all__'
