from django.db import models
import random
import string
from urllib2 import urlopen

# Create your models here.
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

    class Meta:
        verbose_name = 'Mini URL'
        verbose_name_plural = 'Mini URLS'
