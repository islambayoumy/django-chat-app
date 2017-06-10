from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.status)


class Messages(models.Model):

    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    msg = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Messages"
    
    def __str__(self):
        return self.id


