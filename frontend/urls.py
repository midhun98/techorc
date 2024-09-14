from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="register.html"), name="register"),
    path("login/", TemplateView.as_view(template_name="login.html"), name="login"),
    path("secret/", TemplateView.as_view(template_name="secret.html"), name="secret"),
]
