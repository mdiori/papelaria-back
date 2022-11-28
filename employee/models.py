from django.db import models
from core.db.models import SoftDeleteModel
from uuid import uuid4


class Employee(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=128)
    mail = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
