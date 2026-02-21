from django.db import models
# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateField(auto_now=True)
    price = models.DecimalField(decimal_places=10, max_digits=3)