from django.conf import settings
from django.http import HttpResponse


class MaintenanceModeMiddleware:
    """
    Check if site if in maintencace mode
    If the Maintenacemode is True, it returns a "site is under maintenace"
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        if getattr(settings, "MAINTENACE_MODE", False):
            return HttpResponse("Site is under maintenace", status=503)
        return self.get_response(request)
