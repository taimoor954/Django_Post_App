create a mini app like user in django project 
python manage.py startapp <app_name>

inside your main app folder which you created using command there will be a settin file
write your name app name inside INSTALLED_APPS Array like '<app_name>'


inside your mini app there will be a file name models
from django.db import models

class Users(models.Model):
    text= models.CharField(max_length=160, blank=False,null=False)

    def __str__(self) -> str:
        return self.text


There will be a migration folder inside of your mini app inside of it there will be file with 0001_initial.py
inside operation array paste this
 migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=160)),
            ],
        ),



Then go to admin.py file inside your mini app folder
from django.contrib import admin
from .models import Posts
# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts , PostsAdmin)


RUN A COMMAD python manage.py makemigrations
RUN A COMMAD python manage.py migrate
