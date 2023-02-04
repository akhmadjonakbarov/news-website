from django.db import models
import uuid
# Create your models here.


class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self) -> str:
        return str(f'{self.first_name} {self.last_name}')
        
