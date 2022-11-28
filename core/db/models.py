from django.db.models.functions import Now
from django.db.models.signals import pre_delete
from django.db import models, router


class SoftDeleteQueryset(models.QuerySet):
    def delete(self):
        count = 0
        for obj in self:
            pre_delete.send(
                sender=self.model,
                instance=obj,
                using=router.db_for_write(self.model, instance=self)
            )
            obj.deleted_at = Now()
            obj.save()
            count += 1
        return count, {self.model._meta.object_name: count}


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQueryset(
            self.model,
            using=self._db
        ).filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    original_objects = models.Manager()

    def delete(self):
        pre_delete.send(
            sender=self.__class__,
            instance=self,
            using=router.db_for_write(self.__class__, instance=self)
        )
        self.deleted_at = Now()
        self.save()

    class Meta:
        abstract = True
