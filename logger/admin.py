from django.contrib import admin
from django.contrib.postgres import fields
from .models import RequestLog
from django_json_widget.widgets import JSONEditorWidget


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):

    list_display = ('method', 'status_code', 'time', 'user', 'endpoint', 'short_request',
                    'short_response', 'response_time')

    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

    def change_view(self, request, object_id, form_url='', extra_context=None):
        ''' customize edit form '''
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        extra_context['show_save_and_add_another'] = False  # this not works if has_add_permision is True
        return super(RequestLogAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            # All model fields as read_only
            return self.readonly_fields + tuple([item.name for item in obj._meta.fields \
                                                 if item.name not in ['response_body','request_body', 'query_params']])
        return self.readonly_fields
