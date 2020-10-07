from django.urls import path
from users.api.views import UserCreateView, UserLoginAPIView

from rest_framework.authtoken.views import obtain_auth_token

app_name = "users"

urlpatterns = [
    path('register/', UserCreateView.as_view(), name = 'register'),
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
]