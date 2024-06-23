from django.db import models
from django.conf import settings

x = [
    ('Low', 'Low'),
    ('High', 'High'),
    ('Medium', 'Medium')
]


class Task(models.Model):
    
    title = models.CharField(max_length=55, null=True)
    teacher = models.CharField(max_length=55, null=True)
    choose = models.CharField(max_length=6, choices=x, null=True)
    Description = models.TextField(max_length=160, blank=True, null=True)
    completed = models.BooleanField(default=False, null=True)
    admin = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null = True)
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='admin_tasks')
    def __str__(self):
        return self.title