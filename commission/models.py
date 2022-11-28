from django.db import models
from core.db.models import SoftDeleteModel
from uuid import uuid4


class Commission(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    week_day = models.PositiveIntegerField()
    commission_min = models.PositiveIntegerField()
    commission_max = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
