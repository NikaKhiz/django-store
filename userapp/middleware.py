from datetime import datetime
from django.utils.timezone import make_aware
from django.utils.deprecation import MiddlewareMixin

class UpdateUserLastActionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.user.last_active_datetime = make_aware(datetime.now())
            request.user.save(update_fields=['last_active_datetime'])