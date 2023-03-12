from django.db import models

# Create your models here.


class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)

    class Meta:
        ordering = ['created']
