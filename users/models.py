from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    user_id = models.UUIDField( unique=True, default=uuid.uuid4)
    contact_no = models.CharField(max_length=50)

class Customer(models.Model):
    customer_id = models.UUIDField()
    special_notes = models.CharField(max_length=255)
