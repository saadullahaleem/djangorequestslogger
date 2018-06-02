import datetime
import json
from django.template.response import TemplateResponse
from .models import RequestLog
from ipware.ip import get_real_ip


class RequestResponseLogger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_log = RequestLog()
        request_log.method = request.method
        request_log.endpoint = request.path
        request_log.ip = get_real_ip(request)

        try:
            body = json.loads(request.body.decode('utf-8'))
            if 'password' in body:
                body['password'] = 'xxxxxxxx'
            request_body = body
        except Exception as e:
            request_body = {}
        if request.GET:
            request_log.query_params = dict(request.GET)
        if request.body:
            request_log.request_body = request_body
        request_log.time = datetime.datetime.now()
        request_log.save()

        # save a new instance of request log object

        response = self.get_response(request)

        # update instance if response
        if not request.user.is_anonymous():
            # created request_log object ka attr set hoga
            request_log.user = request.user

        try:
            if isinstance(response, TemplateResponse):
                response_body = {'message': str(response.content)}
            elif response.status_code != 500:
                response_body = response.data
            else:
                response_body = {'message': str(response.content)}
        except Exception as e:
            response_body = {'message': str(e)}

        request_log.response_body = response_body
        request_log.status_code = response.status_code
        request_log.response_time = (datetime.datetime.now() - request_log.time).microseconds / 1000
        request_log.save()

        return response
