from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import CreateUserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

# Create your views here.


class CreateTeacherParentView(CreateAPIView):
    serializer_class=CreateUserSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

