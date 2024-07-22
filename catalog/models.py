from django.db import models

from catalog.enum import CategoryName


class Category(models.Model):
    name = models.CharField(max_length=20, choices=CategoryName.as_choices(), default=None,)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Car(models.Model):
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)

    sale_price = models.DecimalField(decimal_places=2, max_digits=8, default=0.00)
    base_price = models.DecimalField(decimal_places=2, max_digits=8, default=0.00, null=True)

    images = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car'
