from django.db import models


class search(models.Model):
    search_url = models.CharField(max_length=1000)
    created = models.TimeField(auto_now=True)
