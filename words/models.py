from django.db import models

# Create your models here.


class Word(models.Model):
    class Meta:
        pass

    text = models.CharField(max_length=128)
    audio = models.FileField(upload_to='words/audios/')

    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.text

