from datetime import datetime
from django.utils.timezone import make_aware
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
from django.shortcuts import redirect


class UpdateUserLastActionMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_authenticated:
            now = make_aware(datetime.now())  
            request.user.last_active_datetime = now
            request.user.save(update_fields=['last_active_datetime'])

        return response
    

class UserActivityCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            now = make_aware(datetime.now())
            last_active = request.user.last_active_datetime
            
            if (now - last_active).total_seconds() > 60:
                request.user.last_active_datetime = now
                request.user.save(update_fields=['last_active_datetime'])
                logout(request)  

                return redirect('store:index')  

