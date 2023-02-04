from rest_framework import serializers
from postapp.models import (Category, SubCategory, Post)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'created_on', 'updated_on')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('name', 'description', 'created_on', 'updated_on')
