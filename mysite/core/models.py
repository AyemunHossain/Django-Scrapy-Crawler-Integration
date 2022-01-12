from django.db import models


class QuotetItem(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    tag = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "Quotet Iteam"
