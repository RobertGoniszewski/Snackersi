from django.db import models
from . import utils

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.TextField(max_length=50, unique=True)
    country_of_origin = models.TextField(max_length=50, default=None)
    description = models.TextField(max_length=1000, default=None, blank=True)
    logo = models.ImageField(upload_to='companies/logos/', unique=True, default=None)
    first_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    ean = models.IntegerField(max_length=13, null=True, help_text='Scan the EAN code of the product.')
    ingredients = models.ManyToManyField('Ingredient', blank=True)
    pictures = models.ManyToManyField('Picture', null=True)
    categories = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tag')
    good_with = models.ManyToManyField('self', blank=True)
    added_by = models.ForeignKey('Author', on_delete=models.CASCADE)
    first_added = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} (id: {self.id})'


class Ingredient(models.Model):
    name = models.TextField(max_length=50, null=True, unique=True)
    calories = models.IntegerField(default=None, help_text='How many kcal per 100g?')
    is_allergen = models.BooleanField(blank=False)
    kind_list = [
        ('g', 'good'),
        ('n', 'neutral'),
        ('h', 'harmful')
    ]
    kind = models.CharField(max_length=1, choices=kind_list, default='n')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000)
    products = models.ManyToManyField('Product', blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    products = models.ManyToManyField('Product', blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, blank=True)
    rating_list = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]
    rating = models.CharField(max_length=1, choices=rating_list, default='5')

    def __str__(self):
        return f'{self.author} - {self.product}'


class Picture(models.Model):
    filename = models.CharField(max_length=20)
    path = models.ImageField(upload_to=utils.path, blank=True)
    added_by = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.filename


