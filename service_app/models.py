from django.db import models

# Create your models here.
class ServiceModel(models.Model):
    service = models.CharField(max_length = 50)

    def __str__(self):
        return self.service