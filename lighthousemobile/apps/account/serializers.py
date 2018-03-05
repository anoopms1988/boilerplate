from core.serializers import ExModelSerializer
from django.contrib.auth.models import User
from .models import AccessApiKey


class UserSerializer(ExModelSerializer):
    class Meta:
        model = User
        exclude = ()


class AccessApiKeySerializer(ExModelSerializer):
    class Meta:
        model = AccessApiKey
        exclude = ()
