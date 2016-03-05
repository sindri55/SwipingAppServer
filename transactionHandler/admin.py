from django.contrib import admin
from transactionHandler import models


# Register your models here.

admin.site.register(models.Transaction)
admin.site.register(models.bankInfo)
admin.site.register(models.userProfile)
