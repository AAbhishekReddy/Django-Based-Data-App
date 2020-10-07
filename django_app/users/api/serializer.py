from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db.models import Q

from rest_framework.authtoken.models import Token

from data_app.models import new_york, beer_review


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField(allow_blank = True, read_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']
        extra_kwargs = {
            'password' : {
                'write_only' : True
                }
        }
    
    def validate(self, data):
        email = data['email']
        user = User.objects.filter(email = email)
        print(user)
        if user.exists():
            raise serializers.ValidationError("This user has already registered.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username = username,
            email = email
        )

        user_obj.set_password(password)
        user_obj.save()
        token = Token.objects.get(user = user_obj).key
        validated_data['token'] = token
        return validated_data

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(required = False, allow_blank = True)
    email = serializers.EmailField(required = False, allow_blank = True)
    token = serializers.CharField(allow_blank = True, read_only = True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', "token"]
        extra_kwargs = {
            'password' : {
                'write_only' : True
                }
        }
    
    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password')
        if not email and username:
            raise serializers.ValidationError("An username or an email is required to login")
        user = User.objects.filter(
            Q(email = email) |
            Q(username = username) 
        ).distinct()

        if user.exists and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("The username or email is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect Credentials")

        token = Token.objects.get(user = user_obj).key
        data['token'] = token
                        

        return data