from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
User = get_user_model()
# Create your views here.


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # data hold request info
        data = self.request.data

        # extract info  from post data
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        # verify passwords
        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exist'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(
                        email=email, password=password, name=name)
                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})
