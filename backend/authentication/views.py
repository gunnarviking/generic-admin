from django.shortcuts import render


# Create your views here.
def login_post(request):
    if request.method == "POST":
        print("hello")
        data = json.loads(request.body.decode("utf-8"))
        email = data.get("email")
        password = data.get("password")
        return JsonResponse({"status": "success", "message": "Login successful"})
