from django.db import models
import time
import os

# Create your models here.


def file_upload(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return filename


class Programming(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    creator = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=file_upload,
                              blank=True, null=True, default='nf.jpg')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'programming'


class Framework(models.Model):
    name = models.CharField(max_length=100)
    programming = models.ForeignKey(
        Programming, on_delete=models.CASCADE, related_name='frameworks')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'framework'
