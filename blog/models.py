from django.conf import settings
from django.db import models
from django.utils import timezone



class Word(models.Model):
    word = models.TextField()
    publish_date = models.DateTimeField(blank = True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(default="описание")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.word
