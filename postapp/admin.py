from django.contrib import admin
from .models import (Category, SubCategory, Post)
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('name', 'category',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_category', 'sub_category',)
    list_filter = ('title', 'main_category', 'sub_category',)