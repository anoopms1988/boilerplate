import logging

from core.viewsets import ExModelViewSet
from rest_framework.permissions import AllowAny
from core import errors as err
from .models import JobForm
from .serializers import JobFormSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)


class JobFormViewSet(ExModelViewSet):
    queryset = JobForm.objects.all()
    serializer_class = JobFormSerializer
