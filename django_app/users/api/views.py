from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token


from rest_framework.generics import CreateAPIView

from users.api.serializer import RegistrationSerializer, LoginSerializer


class UserCreateView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_class = [AllowAny]
    queryset = User.objects.all()

class UserLoginAPIView(APIView):
    permission_class = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = LoginSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            data_cp = {
                'email' : data['email'],
                'username' : data['username'],
            }
            
            user_obj = User.objects.filter(username = data['username'])
            user_obj = user_obj.first()
            token = Token.objects.get(user = user_obj).key
            data_cp['token'] = token

            return Response(data_cp, status = HTTP_200_OK)
        return Response(serializer.errors, statis = HTTP_400_BAD_REQUEST)