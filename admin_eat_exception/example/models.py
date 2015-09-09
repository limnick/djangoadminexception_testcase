from django.db import models


class BookModel(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
