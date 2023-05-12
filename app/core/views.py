from urls.models import URL
from rest_framework.decorators import api_view
from django.shortcuts import redirect


def get_redirect_url(pid):
    qs = URL.objects.filter(pid=pid)
    if qs:
        instance = qs[0]
        long_url = instance.long_url
        return long_url
    
    return ""


@api_view(["GET"])
def redirect_to_site(request, *args, **kwargs):
    pid = kwargs.get("pid")

    redirect_url = get_redirect_url(pid)
    return redirect(redirect_url)    
