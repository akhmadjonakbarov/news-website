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
    view = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)

    def get_images(self):
        return self.set_images.all()


    def updated_views(self, *args, **kwargs):
        self.view = self.view + 1
        super(Post, self).save(*args, **kwargs)



class PostImages(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="set_images")
    image = models.FileField(upload_to="post-images")

    def __str__(self) -> str:
        return (self.post.title) 
