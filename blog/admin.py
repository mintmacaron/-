from django.contrib import admin

from. models import Blog
# Register your models here.

admin.site.register(Blog)
from. models import Comment

admin.site.register(Comment)