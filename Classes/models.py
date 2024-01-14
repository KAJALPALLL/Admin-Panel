from django.db import models


class Classes(models.Model):
    title = models.TextField(default=None, null=True)
    description = models.TextField(default=None, null=True)
    image = models.ImageField(upload_to='class/', default=None, null=True)
    url = models.URLField(default=None, null=True)
    status = models.BooleanField(default=0)
