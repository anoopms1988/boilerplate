from django.db import models
from core.models import ExModel
from core import helper
from .constants import AccessApiKey


# Create your models here.

class AccessApiKey(ExModel):
    """
    Class Model for Access API Key
    """
    ACCESS_TYPES = helper.prop2pair(AccessApiKey)
    type = models.TextField(choices=ACCESS_TYPES, null=False, blank=False)
    key = models.TextField(null=False, blank=False)

    def __str__(self):
        return "%s" % (self.type)
