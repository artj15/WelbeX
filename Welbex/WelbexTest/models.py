from django.db import models


# Create your models here.
class Table(models.Model):
    data = models.DateField()
    name = models.CharField(max_length=1000)
    number = models.IntegerField()
    distance = models.CharField(max_length=1000)

    class Meta:
        ordering = ['data']
        verbose_name = 'WelbeXTable'

    def __str__(self):
        return f'{self.name} {self.data}'
