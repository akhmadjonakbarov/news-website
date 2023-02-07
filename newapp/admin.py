from django.contrib import admin
from .models import (Category, SubCategory, New, NewImages, Comment)
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('name', 'category',)


class NewImagesAdmin(admin.StackedInline):
    model = NewImages
    extra = 3


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_category',)
    list_filter = ('title',  'sub_category',)
    inlines = (NewImagesAdmin,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('body', 'new',)
