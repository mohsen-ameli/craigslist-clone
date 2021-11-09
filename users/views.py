from crum import get_current_user
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy


class LoginClassView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse_lazy("main:home")


class LogoutClassView(LogoutView):
    template_name = "users/logout.html"

    def get_success_url(self):
        return reverse_lazy("main:home")


def CartView(request):
    return render(request, "users/cart.html")
