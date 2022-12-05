from django.db import models
from sorl.thumbnail import ImageField


class Posts(models.Model):
    text = models.CharField(max_length=160, blank=False, null=False)
    image = ImageField()

    def __str__(self) -> str:
        return self.text
