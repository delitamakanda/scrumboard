from django.contrib import admin
from .models import List, Card, Todo

# Register your models here.

admin.site.register(Card)
admin.site.register(List)
admin.site.register(Todo)
