from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Transaction(models.Model):
    owner = models.ManyToManyField(User)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date = datetime.datetime.now()
        return super(Transaction, self).save(*args, **kwargs)


class bankInfo(models.Model):
    owner = models.ManyToManyField(User)
    bankName = models.CharField(max_length=255, null=True)
    iban = models.CharField(max_length=255)
    swift = models.CharField(max_length=255)
