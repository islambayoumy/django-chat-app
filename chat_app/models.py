from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):

    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user


class Messages(models.Model):

    sender = models.ForeignKey(Users, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, related_name="receiver", on_delete=models.CASCADE)
    msg = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Messages"
    
    def __str__(self):
        return self.id


