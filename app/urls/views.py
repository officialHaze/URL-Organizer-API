from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import URL, SingleLink
from django.db import DatabaseError, OperationalError
import shortuuid
import os
import re


def are_valid_urls(urls):
    regex = ("((http|https)://)" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    pattern = re.compile(regex)
    statuses = []
    for url in urls:
        status = re.search(
            pattern,
            url,)
        statuses.append(status)
    
    if None not in statuses:
        return True
    return False


'''handler function to create short url'''
def create_short_url(long_url):
    '''create a short uuid object'''
    su = shortuuid.ShortUUID()
    '''create a random short id of 4 chars'''
    short_id = su.random(length=4)
    short_url = f'http://{os.environ.get("HOST")}:{os.environ.get("PORT")}/{short_id}/'
    
    '''update the database'''
    short_url_instance = update_db(pid=short_id, sh_url=short_url, ln_url=long_url)
    return short_url_instance


'''create a single link for all the short urls'''
def create_single_link(short_urls):
    su = shortuuid.ShortUUID()
    '''create a random uuid of 8 chars'''
    id = su.random(length=8)
    single_link = f'http://{os.environ.get("HOST")}:{os.environ.get("PORT")}/{id}/'

    '''uddate the Single Link DB'''
    update_singlelink_db(id=id, single_link=single_link, short_urls=short_urls)
    return single_link


'''helper function to update the database'''
def update_db(pid, sh_url, ln_url):
    try:
        instance = URL.objects.create(pid=pid, long_url=ln_url, short_url=sh_url)
        return instance
    except (DatabaseError, OperationalError):
        if DatabaseError:
            raise DatabaseError
        raise OperationalError


'''helper function to update the single link database'''
def update_singlelink_db(id, single_link, short_urls):
    try:
        for url in short_urls:
            SingleLink.objects.create(short_id=id, single_link=single_link, short_url=url)
    except (DatabaseError, OperationalError):
        if DatabaseError:
            raise DatabaseError
        raise OperationalError


@api_view(["POST"])
def organize_urls(req, *args, **kwargs):
    long_urls = req.data.get('long_urls')
   #check to see if the url is a valid url 
    if are_valid_urls(long_urls):
        short_url_list = []
        for url in long_urls:
            '''check wether the url already exists in db'''
            qs = URL.objects.filter(long_url = url)
            #if it does get the short url and append it to the list
            if qs:
                short_url_instance = qs[0]
                short_url_list.append(short_url_instance)
            #if not create a short url then append it to the list
            else:
                short_url = create_short_url(url)
                short_url_list.append(short_url)
        if len(short_url_list) == 1:
            single_link = short_url_list[0].short_url
        else:
            single_link = create_single_link(short_url_list)
        return Response({'single_link':single_link}, status=200)
    
    return Response({'details':'invalid url!'}, status=400)

