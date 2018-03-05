from django.db import models
from core.models import ExModel
from core import helper


class JobForm(ExModel):
    """
    Class model for Job Form
    """
    name = models.CharField(max_length=200, null=False, blank=False)
    jnid = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    fields = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)
