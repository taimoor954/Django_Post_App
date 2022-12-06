from django.db import models
from sorl.thumbnail import ImageField


class Posts(models.Model):
    text = models.CharField(max_length=170, blank=False, null=False)
    image = ImageField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.text
