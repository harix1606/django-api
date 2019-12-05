from django.db import models

class Songs(models.Model):
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, default = 'classical')

    def __str__(self):
        return self.name
