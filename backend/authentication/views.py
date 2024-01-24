from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from json import loads
from django.http import HttpResponse
from django.contrib.auth import authenticate


@csrf_exempt
def login_post(request):
    if request.method == "POST":
        data = loads(request.body.decode("utf-8"))
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=403)
