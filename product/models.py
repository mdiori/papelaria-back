from django.db import models
from core.db.models import SoftDeleteModel
from uuid import uuid4


class Product(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    value = models.PositiveIntegerField()
    commission = models.PositiveIntegerField()
    code = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
