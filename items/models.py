from django.db import models
import uuid

# Create your models here.
class Item(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=50)
    price = models.FloatField()