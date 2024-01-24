# myapp/urls.py
from django.urls import path
from .views import login_post

urlpatterns = [
    path("login/", login_post, name="create_post"),
    # Add other URL patterns as needed
]
