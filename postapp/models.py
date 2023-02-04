# python library
import uuid

# django library
from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_subcategorues(self) -> list:
        return self.set_subcategories.all()


class SubCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,  related_name="set_subcategories",)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_post(self) -> list:
        return self.set_sub_post.all()


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    main_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="set_post")
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="set_sub_post")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)
