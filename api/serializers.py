from rest_framework import serializers
from postapp.models import (Category, SubCategory, Post, PostImages)
from contactapp.models import Contact


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'sub_categories',
                  'created_on', 'updated_on')

    def get_sub_categories(self, obj: Category):

        sub_categories = obj.set_subcategories.all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        return serializer.data


class SubCategorySerializer(serializers.ModelSerializer):
    news = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'description',
                  'news', 'created_on', 'updated_on')

    def get_news(self, obj: SubCategory):
        news = obj.set_sub_post.all()
        serializer = PostSerializer(news, many=True)
        return serializer.data


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_images(self, new: Post):
        images = new.get_images()
        serializer = PostImagesSerializer(images, many=True)
        return serializer.data


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'body')
