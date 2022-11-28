from django.db import models
from core.db.models import SoftDeleteModel
from client.models import Client
from employee.models import Employee
from product.models import Product
from uuid import uuid4


class Sale(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    date = models.DateTimeField()
    commission_min = models.PositiveIntegerField(default=0)
    commission_max = models.PositiveIntegerField(default=10)
    invoice = models.CharField(max_length=128)

    # ForeignKeys
    client = models.ForeignKey(Client, models.CASCADE)
    employee = models.ForeignKey(Employee, models.CASCADE)

    class Meta:
        ordering = ['date', ]


class SaleProduct(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    quantity = models.PositiveIntegerField()
    sale = models.ForeignKey(Sale, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
