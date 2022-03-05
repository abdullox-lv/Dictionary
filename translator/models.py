from django.db import models

# Create your models here.


class Dictionary(models.Model):

    english = models.CharField("English word", max_length=100)
    uzbek = models.CharField("Uzbek word", max_length=100)