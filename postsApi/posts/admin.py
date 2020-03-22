from django.contrib import admin

# Register your models here.
from .models import Post, Boast
admin.site.register(Post)
admin.site.register(Boast)
