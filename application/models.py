from django.db import models
import datetime

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    port = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    key_1 = models.CharField(max_length=200)
    key_2 = models.CharField(max_length=200)
    key_3 = models.CharField(max_length=200)

    def __str__(self):
        info = str(self.name)+' ---- '+str(self.host)
        return info
	

class ConnectionObject(models.Model):
    obj_name = models.CharField(max_length=200)
    obj_value = models.CharField(max_length=200)
    obj_timestamp = models.TimeField(datetime.datetime.now())

    def __str__(self):
        info = str(self.obj_name)+' ---- '+str(self.obj_value)+' ---- '+str(self.obj_timestamp)
        return info