from django.contrib import admin
from .models import List, Card, Todo

# Register your models here.
@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created']

admin.site.register(Card)
