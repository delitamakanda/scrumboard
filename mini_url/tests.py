from django.test import TestCase
from mini_url.models import MiniUrl

# Create your tests here.
def setUp(self):
  MiniUrl.objects.create(url="http://www.google.com", code="451x41")
  MiniUrl.objects.create(url="http://www.yahoo.fr", code="884g45")
  
def test_miniurl_can_create(self):
  gogole = MiniUrl.objects.get(url="http://www.google.com")
  yahoo = MiniUrl.objects.get(url="http://www.yahoo.fr")
  self.assertEqual(gogole.create(), 'code gogole is "451x41"')
  self.assertEqual(yahoo.create(), 'code yahoo is "884g45"')
  
  
