from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Types(models.Model):
    typeName = models.TextField(max_length=200, null=True)
    user = models.ManyToManyField(User, null=True)

    def __str__(self):
        return self.typeName


class Todo(models.Model):
    title = models.TextField(max_length=100,  null=True)
    content = models.TextField(max_length=500,  null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    typeTodo = models.ForeignKey(Types, null=True, on_delete=models.CASCADE)
    completed = models.BooleanField(null=True)
    due_date = models.DateField(null=True, auto_now=False, auto_now_add=False)

    #  models.DateTimeField(
    #     null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
