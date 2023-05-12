from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import URL
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
def create_short_url(long_urls):
    '''create a short uuid object'''
    su = shortuuid.ShortUUID()
    '''create a random short id of 8 chars'''
    short_id = su.random(length=8)
    short_url = f'http://{os.environ.get("HOST")}:{os.environ.get("PORT")}/{short_id}/'

    '''update the database'''
    update_db(pid=short_id, sh_url=short_url, ln_urls=long_urls)

    return short_url


'''helper function to update the database'''
def update_db(pid, sh_url, ln_urls):
    for i in range(len(ln_urls)):
        instance = URL.objects.update_or_create(pid=pid, long_url=ln_urls[i], short_url=sh_url)

@api_view(["POST"])
def shorten_url(req, *args, **kwargs):
    long_urls = req.data.get('long_urls')
    print(long_urls)

   #check to see if the url is a valid url 
    if are_valid_urls(long_urls):
        short_urls = []
        pids = []
        '''check to see if the long urls already exist in db'''
        for url in long_urls:
            qs = URL.objects.filter(long_url=url)
            if qs:
                instance = qs[0]
                short_urls.append(instance.short_url)
                pids.append(instance.pid)
        if len(short_urls) is not 0:
            short_url = short_urls[0]
            update_db(pids[0], short_urls[0], long_urls)
        else:
            short_url = create_short_url(long_urls)

        return Response({'short_url':short_url}, status=200)
    
    return Response({'details':'invalid url!'}, status=400)

