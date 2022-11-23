from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Title(models.Model):
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=150)
    date_added = models.DateTimeField()
    verses = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'title'

    def __str__(self):
        return self.title


class Entry(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField()
    verse = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."