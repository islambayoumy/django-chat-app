from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat_app.models import UserProfile, Messages
from chat_app.serializers import UserProfileSerializer
#import requests, json
#from django.db.models import Q

class UsersList(APIView):

    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post():
        pass

