from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/')

    def __str__(self):
        return self.user.first_name


class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Task: {self.title } (For {self.assigned_to})'
