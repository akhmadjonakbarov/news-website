from rest_framework import serializers
from newapp.models import (Category, SubCategory, New, NewImages, Comment)
from sliderapp.models import Slider
from contactapp.models import Contact
from accountapp.models import Account

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'sub_categories',
                  'created_on', 'updated_on',)

    def get_sub_categories(self, obj: Category):
        sub_categories = obj.set_subcategories.all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        return serializer.data


class SubCategorySerializer(serializers.ModelSerializer):
    news = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'description',
                  'news', 'created_on', 'updated_on',)

    def get_news(self, obj: SubCategory):
        news = obj.set_news.all()
        serializer = NewSerializer(news, many=True)
        return serializer.data


class NewSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = New
        fields = '__all__'

    def get_images(self, new: New):
        images = new.get_images()
        serializer = NewImagesSerializer(images, many=True)
        return serializer.data
    
    def get_comments(self, new:New):
        comments = new.get_comments()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


class NewImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewImages
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'body',)

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username',
            'first_name', 'last_name',
        )



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password= serializers.CharField()