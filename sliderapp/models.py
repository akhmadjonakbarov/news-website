from django.db import models
from ckeditor.fields import RichTextField
class Slider(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()
    image = models.FileField(upload_to="slider-images")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)