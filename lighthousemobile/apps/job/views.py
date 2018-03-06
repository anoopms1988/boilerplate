import logging
import requests
import urllib.parse
import logging
import json

from core.viewsets import ExModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route, \
    list_route, permission_classes
from core import errors as err
from .models import JobForm
from .serializers import JobFormSerializer
from apps.account.models import AccessApiKey

# Get an instance of a logger
logger = logging.getLogger(__name__)


class JobFormViewSet(ExModelViewSet):
    queryset = JobForm.objects.all()
    serializer_class = JobFormSerializer

    @list_route(methods=['GET'])
    def job_list(self, request):
        try:
            admin_api_key = AccessApiKey.objects.filter(type='admin').first().key
            if not admin_api_key:
                raise err.ValidationError(*("No admin api key exist", 400))
            bearer_token = 'Bearer' + ' ' + admin_api_key
            headers = {'Authorization': bearer_token}
            #filter = {"must": [{"term": {"sales_rep_name": "anila vasudevan"}}]}
            filter={}
            start = int(request.query_params.get('start', 1)) * 10 - 10
            url = 'https://app.jobnimbus.com/api1/jobs?size=10&from=' + str(start) + "&filter=" +\
                  urllib.parse.quote(
                    str(filter)).replace('%27', '%22')
            result = requests.get(url=url, headers=headers)
            return Response(json.loads(result.text))
        except Exception as e:
            logger.error(e.message)
            raise err.ValidationError(*(e.message, 400))

    @list_route(methods=['GET'])
    def specific_job(self, request):
        try:
            admin_api_key = AccessApiKey.objects.filter(type='admin').first().key
            if not admin_api_key:
                raise err.ValidationError(*("No admin api key exist", 400))
            bearer_token = 'Bearer' + ' ' + admin_api_key
            headers = {'Authorization': bearer_token}
            jnid = request.query_params.get('jnid', None)
            if not jnid:
                raise err.ValidationError(*("Specific job id not given", 400))
            url = 'https://app.jobnimbus.com/api1/jobs/' + str(jnid)
            result = requests.get(url=url, headers=headers)
            return Response(json.loads(result.text))
        except Exception as e:
            logger.error(e.message)
            raise err.ValidationError(*(e.message, 400))

    @list_route(methods=['GET'])
    def forms_list(self, request):
        try:
            jnid = request.query_params.get('jnid', None)
            if not jnid:
                raise err.ValidationError(*("Specific job id not given", 400))
            job_forms = JobForm.objects.filter(jnid=jnid).all()
            serialized = JobFormSerializer(job_forms, many=True).data
            return Response(serialized)
        except Exception as e:
            logger.error(e.message)
            raise err.ValidationError(*(e.message, 400))
