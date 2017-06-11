from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat_app.models import UserProfile, Messages
from django.contrib.auth.models import User
from chat_app.serializers import UserProfileSerializer, MessagesSerializer
from django.db.models import Q


class UsersList(APIView):

    def get(self, request):
        userId = request.GET.get('userId')
        users = UserProfile.objects.exclude(user=userId)
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post():
        pass


class MessagesList(APIView):

    def get(self, request):
        fromId = request.GET.get('fromId')
        toId = request.GET.get('toId')
        query = Q(Q(sender=fromId)&Q(receiver=toId))|Q(Q(sender=toId)&Q(receiver=fromId))
        msgs = Messages.objects.filter(query).order_by('timestamp')
        serializer = MessagesSerializer(msgs, many=True)
        return Response(serializer.data)

    def post(self, request):
        fromId = request.POST.get('fromId', '')
        toId = request.POST.get('toId', '')
        msg = request.POST.get('msg', '')

        sender_user = User.objects.get(pk=fromId)
        receiver_user = User.objects.get(pk=toId)

        try:
            msg_obj = Messages.objects.create(sender=sender_user, receiver=receiver_user, msg=msg)
            msg_obj.save()
            return Response('add successfully', status=status.HTTP_201_CREATED)
        except:
            return Response('error')


