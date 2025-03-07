from django.db import models

class Operation(models.Model):
    value = models.FloatField()
    converted_value = models.FloatField(null=True, blank=True)
    to_unit = models.CharField(max_length=10)