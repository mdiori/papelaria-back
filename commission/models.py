from django.db import models
from core.db.models import SoftDeleteModel
from uuid import uuid4


class Commission(SoftDeleteModel):

    class WEEK_DAY(models.IntegerChoices):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    week_day = models.PositiveIntegerField(choices=WEEK_DAY.choices)
    commission_min = models.PositiveIntegerField(default=0)
    commission_max = models.PositiveIntegerField(default=1000)

    class Meta:
        ordering = ['week_day', ]
        constraints = [
            models.UniqueConstraint(
                fields=['week_day', ],
                condition=models.Q(deleted_at=None),
                name='unique_week_day_if_not_deleted'
            ),
        ]
