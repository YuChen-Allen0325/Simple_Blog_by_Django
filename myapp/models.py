from django.db import models
from datetime import datetime
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 100)
    body  = models.CharField(max_length= 10000)
    create_at = models.DateTimeField(default= datetime.now, blank = True)
