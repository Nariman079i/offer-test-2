from django.db import models
from django.core import validators


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название товара")
    count = models.IntegerField(validators=[
        validators.MinValueValidator(0, message="Количество товара не должно быть меньше 0"),
    ], verbose_name="Количество товара")
    unit = models.CharField(max_length=10, verbose_name="Единица измерения", choices=(
        ('gr', 'Грамм'),
        ('kg', 'Килограмм'),
        ('ob', 'Штук'),
        ('st', 'Упаковок'),
    ))

    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория товара")
    description = models.TextField(verbose_name="Описание товара")


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.title