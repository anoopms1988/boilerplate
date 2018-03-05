import logging

from core.serializers import ExModelSerializer
from .models import JobForm
from core import errors as err

# Get an instance of a logger
logger = logging.getLogger(__name__)


class JobFormSerializer(ExModelSerializer):
    class Meta:
        model = JobForm
        exclude = ()


# class JobFormCreateSerializer(ExModelSerializer):
#     class Meta:
#         model = JobForm
#         exclude = ()
#
#     def validate(self, attrs):
#         return attrs
#
#     def create(self, validated_data):
#         try:
#             jobform_serializer = JobFormSerializer(data=validated_data)
#             if jobform_serializer.is_valid(raise_exception=True):
#                 jobform = jobform_serializer.save()
#             return jobform
#         except Exception as e:
#             logger.error(e.message)
#             raise err.ValidationError(*(e.message, 400))
#
#     def update(self, instance, validated_data):
#         try:
#             pass
#         except Exception as e:
#             logger.error(e.message)
#             raise err.ValidationError(*(e.message, 400))
