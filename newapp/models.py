from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    name = models.CharField(max_length=250)
    description = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_subcategorues(self) -> list:
        return self.set_subcategories.all()


class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    description = RichTextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,  related_name="set_subcategories",)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_post(self) -> list:
        return self.set_sub_post.all()


class New(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="set_news")
    view = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)

    def get_images(self):
        return self.set_images.all()
    
    def get_comments(self):
        return self.set_comments.all()

    def updated_views(self, *args, **kwargs):
        self.view = self.view + 1
        super(New, self).save(*args, **kwargs)


class NewImages(models.Model):
    post = models.ForeignKey(
        New, on_delete=models.CASCADE, related_name="set_images")
    image = RichTextUploadingField()

    def __str__(self) -> str:
        return (self.post.title)

class Comment(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name="set_comments")
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.body)[:60]