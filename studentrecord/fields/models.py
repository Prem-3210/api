from django.db import models

class Fields(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True, default=0)
    classname = models.CharField(max_length=100, null=True, blank=True)
    marks = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name
