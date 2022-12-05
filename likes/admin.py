from django.contrib import admin
from .models import Likes

# Register your models here.
class LikesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Likes , LikesAdmin)