from django.http import HttpResponse
from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)