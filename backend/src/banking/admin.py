from django.contrib import admin
from .models import Bank, Account, Transaction, UserBank

admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(UserBank)