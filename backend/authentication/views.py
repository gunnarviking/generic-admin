from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from json import loads
from django.http import JsonResponse


@csrf_exempt
def login_post(request):
    if request.method == "POST":
        print("hello")
        data = loads(request.body.decode("utf-8"))
        email = data.get("email")
        password = data.get("password")
        return JsonResponse({"status": "success", "message": "Login successful"})
