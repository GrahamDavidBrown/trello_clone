from django.contrib import admin
from .models import Card, List, Board, UserProfile

# Register your models here.
admin.site.register(Card)
admin.site.register(List)
admin.site.register(Board)
admin.site.register(UserProfile)
