from datetime import datetime

from django.db import models
from django.utils.timezone import now


class Message(models.Model):
    content = models.TextField(max_length=1000)
    messenger = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content
