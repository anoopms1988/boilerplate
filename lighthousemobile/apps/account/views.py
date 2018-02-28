import requests
import json
import urllib.parse
import logging

from core.viewsets import ExModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer, \
    AccessApiKeySerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route, \
    list_route, permission_classes
from .models import AccessApiKey
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from core import errors as err

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Get an instance of a logger
logger = logging.getLogger(__name__)


@permission_classes((AllowAny,))
class AccountViewSet(ExModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    retrieve_serializer_class = UserSerializer

    @list_route(methods=['POST'])
    def auth(self, request):
        try:
            username = request.data.get('username', None)
            password = request.data.get('password', None)
            if username is None or password is None:
                raise err.ValidationError(*("Username or password is not given", 400))
            user = authenticate(username=username, password=password)
            if user is not None:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({
                    "token": token,
                    "status": "success",
                })
            else:
                return Response({
                    "status": "failure",
                    "msg": "Invalid parameters"
                })
        except Exception as e:
            logger.error(e.message)
            raise err.ValidationError(*(e.message, 400))

    @list_route(methods=['GET'])
    def jobs_list(self, request):
        try:
            headers = {'Authorization': 'Bearer jdwuekh380tc34fq'}
            filter = {"must": [{"term": {"is_completed": 'true'}}]}
            params = {"filter": filter}
            url = 'https://app.jobnimbus.com/api1/jobs'
            result = requests.get(url=url,
                                  params=urllib.parse.quote(str(params)), headers=headers)
            # result = requests.get(url=url, headers=headers)
            return Response(json.loads(result.text))
        except Exception as e:
            logger.error(e.message)
            raise err.ValidationError(*(e.message, 400))

    @list_route(methods=['GET'])
    def specific_job(self, request):
        try:
            headers = {'Authorization': 'Bearer jdwuekh380tc34fq'}
            jnid=request.query_params.get('jnid',None)
            url = 'https://app.jobnimbus.com/api1/jobs/'+str(jnid)
            # result = requests.get(url=url,
            #                       params=urllib.parse.quote(str(params)), headers=headers)
            result = requests.get(url=url, headers=headers)
            return Response(json.loads(result.text))
        except Exception as e:
            logger.error(e.message)
            raise err.ValidationError(*(e.message, 400))

    def get_queryset(self):
        try:
            queryset = User.objects.all()
            return queryset
        except Exception as e:
            pass


class AccessApiKeyViewSet(ExModelViewSet):
    queryset = AccessApiKey.objects.all()
    serializer_class = AccessApiKeySerializer
