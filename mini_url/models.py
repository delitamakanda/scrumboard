from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class List(models.Model):
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
