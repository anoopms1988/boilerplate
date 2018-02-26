import requests
import json
import urllib

from django.shortcuts import render
from core.viewsets import ExModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer, \
    AccessApiKeySerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .models import AccessApiKey


class AccountViewSet(ExModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    retrieve_serializer_class = UserSerializer

    @list_route(methods=['GET'])
    def jobs_list(self, request):
        try:
            headers = {'Authorization': 'Bearer jdwuekh380tc34fq'}
            filter = {
                "is_completed": True
            }
            condition = json.dumps(filter)
            params = {'size': 100, 'from': 1}
            url = 'https://app.jobnimbus.com/api1/jobs'
            result = requests.get(url=url,
                                  params=params, headers=headers)
            return Response(json.loads(result.text))
        except Exception as e:
            pass

    def get_queryset(self):
        try:
            queryset = User.objects.all()
            return queryset
        except Exception as e:
            pass


class AccessApiKeyViewSet(ExModelViewSet):
    queryset = AccessApiKey.objects.all()
    serializer_class = AccessApiKeySerializer
