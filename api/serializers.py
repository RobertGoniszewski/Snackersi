from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']
        # read_only_fields = ['name', 'email']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'country_of_origin', 'description', 'logo', 'first_added']
        read_only_fields = ['first_added', 'logo']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'company', 'description', 'ean', 'ingredients', 'pictures', 'categories',
                  'tags', 'good_with', 'added_by', 'first_added', 'last_update']
        read_only_fields = ['first_added', 'last_update', 'pictures']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'calories', 'is_allergen', 'kind']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'author', 'product', 'comment', 'rating']
        read_only_fields = []


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['id', 'filename', 'path', 'added_by']
