from django.db import models

# Create your models here.

# Task model to Store task in database
class Task(models.Model):
    title = models.CharField(max_length=555)
    date = models.DateField()
    progress = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


# Imprint model to Store imprint in database
class Imprint(models.Model):
    authors = models.CharField(max_length=555)

    def __str__(self):
        return self.authors