from django.urls import path
from authapp.views import LogUs, RegUs

urlpatterns = [
    path('login/', LogUs.as_view(), name='login'),
    path('register/', RegUs.as_view(), name='register'),
]