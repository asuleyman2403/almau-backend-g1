from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return 'ID: {}, name: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    code = models.CharField(max_length=32, null=False, unique=True)
    name = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return 'ID: {}, name: {}, code: {}'.format(self.id, self.name, self.code)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'category': self.category.to_json()
        }
