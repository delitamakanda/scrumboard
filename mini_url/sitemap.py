import datetime
from django.contrib.sitemaps import Sitemap
from mini_url.models import MiniUrl

class MiniUrlSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return MiniUrl.objects.all()

    def lastmod(self, obj):
        return obj.date
