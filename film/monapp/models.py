from django.db import models

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    style = models.CharField(max_length=100, default='unknown')
    director = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title