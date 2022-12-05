from django.db import models

# Create your models here.
class Likes(models.Model):
    likeCount= models.IntegerField()

    # def __str__(self) -> int:
    #     return self.likeCount