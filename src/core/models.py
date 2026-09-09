from django.db import models

class PageVisit(models.Model):
    # db table
    # id Primary key(auto_generated)
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
# Create your models here.
