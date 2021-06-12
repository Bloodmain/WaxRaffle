from django.db import models
import datetime

# Create your models here.


class Pack(models.Model):
    active = models.BooleanField(default=True, verbose_name='Active')
    start_date = models.DateField(verbose_name='Start_date', default=datetime.datetime.now)
    end_date = models.DateField(verbose_name='End_date')
