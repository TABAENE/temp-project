from __future__ import unicode_literals

from django.db import models

class BlogModel(models.Model):
    comment = models.TextField(max_length=2000)
    posted_date = models.DateField(db_index=True, auto_now_add=True)
    author = models.CharField(max_length=20)
