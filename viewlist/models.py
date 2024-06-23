from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Task(models.Model):
    Taskiid = models.IntegerField(null=True)
    title = models.CharField(max_length=55,null=True)
    teacher = models.CharField(max_length=55,null=True)
    choose = models.CharField(max_length=50)
    Description = models.TextField(max_length=160, blank=True, null=True)
    admin = models.CharField(max_length=15,null=True)
    completed = models.BooleanField(default=False,null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
