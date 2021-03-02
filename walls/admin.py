from django.contrib import admin
from .models import *

admin.site.register(Wall)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Following)
