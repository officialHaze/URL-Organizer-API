from urls.models import URL, SingleLink
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from .site_logos import LOGOS
import urllib.parse


def get_redirect_url(pid):
    qs = URL.objects.filter(pid=pid)
    if qs:
        instance = qs[0]
        long_url = instance.long_url
        return long_url 
    return ""


'''get the site logo'''
def get_site_logo(site_sh_url):
    site_url = URL.objects.filter(short_url=site_sh_url)[0].long_url
    parts = urllib.parse.urlsplit(site_url)
    hostname = parts.netloc
    split_hostname = hostname.rsplit(".")
    if len(split_hostname) >= 3:
        sitename = split_hostname[1]
    else:
        sitename = split_hostname[0]
    logo = "https://www.pngfind.com/pngs/m/301-3010160_free-png-camera-icon-classic-camera-transparent-png.png"
    for logo_detail in LOGOS:
        logo_name = logo_detail.get("name")
        if logo_name == sitename:
            logo = logo_detail.get("logo")
    return logo


def get_links(sid):
    qs = SingleLink.objects.filter(short_id=sid)
    links = []
    for instance in qs:
        short_url_instance = instance.short_url
        logo = get_site_logo(short_url_instance.short_url)
        link_info = {
            "link": short_url_instance.short_url,
            "logo": logo,
        }
        links.append(link_info)
    return links


@api_view(["GET"])
def redirect_to_site(request, *args, **kwargs):
    _id = kwargs.get("pid")
    _id_length = len(_id)
    if _id_length == 4:
        redirect_url = get_redirect_url(_id)
        return redirect(redirect_url)
    link_list = get_links(_id)
    return Response({'links':link_list}, status=200)
