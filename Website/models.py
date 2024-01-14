from django.db import models



class Website(models.Model):
    title = models.TextField(default=None, null=True)
    description = models.TextField(default=None, null=True)
    image = models.ImageField(upload_to='website/', default=None, null=True)
    author = models.TextField(default=None, null=True)
    status = models.BooleanField(default=0)

