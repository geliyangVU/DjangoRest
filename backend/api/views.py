from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import json



def api_home(request, *args, **kwargs):
    body = request.body
    data={}
    try:
        data = json.loads(body)  # string of Json data -> Python Dictionary
    except:
        pass
    print(data)

    data['headers'] = dict(request.headers)
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)