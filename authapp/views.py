from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView


class LogUs(LoginView):
    pass


class RegUs(CreateView):
    pass
