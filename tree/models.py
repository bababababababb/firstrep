from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name