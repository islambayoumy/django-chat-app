from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat_app.models import UserProfile, Messages
from chat_app.serializers import UserProfileSerializer


class UsersList(APIView):

    def get(self, request):
        userId = request.GET.get('userId')
        users = UserProfile.objects.exclude(user=userId)
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post():
        pass

