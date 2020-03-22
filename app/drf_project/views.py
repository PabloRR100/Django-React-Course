from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong CICD!"}
    return JsonResponse(data)
