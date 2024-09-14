from django.urls import path

from . import views

urlpatterns = [
    path("secret/", views.secret, name="secret"),
    path("register/", views.RegisterUserAPIView.as_view(), name="register"),
]
