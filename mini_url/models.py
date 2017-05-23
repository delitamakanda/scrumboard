from django.db import models
import random
import string
from urllib2 import urlopen
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class MiniUrl(models.Model):
    url = models.URLField(verbose_name="URL a reduire", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date:")
    pseudo = models.CharField(max_length=255, blank=True, null=True)
    nb_acces = models.IntegerField(default=0, verbose_name="Nombre d'acces a l'URL")

    def __unicode__(self):
        return u"[{0}] {1}".format(self.code, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generer(6)

        super(MiniUrl, self).save(*args, **kwargs)

    def generer(self, N):
        caracteres = string.ascii_letters + string.digits
        #caracteres = urllib.request.urlretrieve()
        aleatoires = [random.choice(caracteres) for _ in range(N)]

        self.code = ''.join(aleatoires)

    def get_absolute_url(self):
        #return reverse('url', kwargs={'url': self.url})
        return "/%s" %(self.code)

    class Meta:
        verbose_name = 'Mini URL'
        verbose_name_plural = 'Mini URLS'
