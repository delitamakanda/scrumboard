from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, related_name='lists', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "List : {}".format(self.name)

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    extra = models.CharField(max_length=50, blank=True, null=True)
    list = models.ForeignKey(List, related_name='cards')
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Card : {}".format(self.title)


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='todos', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "Todo : {}".format(self.name)

