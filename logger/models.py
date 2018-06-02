from django.contrib.postgres.fields import JSONField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import truncatechars


class RequestLog(models.Model):
    ip = models.CharField(null=True, max_length=20)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    method = models.CharField(max_length=10)
    request_body = JSONField(null=True)
    query_params = JSONField(null=True)
    endpoint = models.CharField(max_length=200)
    time = models.DateTimeField()
    response_body = JSONField(null=True)
    response_time = models.IntegerField(null=True)
    status_code = models.CharField(null=True, max_length=5)

    @property
    def short_request(self):
        return truncatechars(self.request_body, 100)

    @property
    def short_response(self):
        return truncatechars(self.response_body, 100)
