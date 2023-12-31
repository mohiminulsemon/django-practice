from django.contrib import admin
from .models import UserAddress, UserBankAccount
# Register your models here.

admin.site.register(UserAddress)
admin.site.register(UserBankAccount)