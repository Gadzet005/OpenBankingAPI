from django.contrib.auth import get_user_model
from django.db import models
from users.models import CustomUser
from django.db.models import UniqueConstraint
from datetime import datetime

User = get_user_model()


class Bank(models.Model):
    name = models.CharField(max_length=30)
    bank_code = models.IntegerField(unique=True)
    api_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_code = models.IntegerField()
    isHide = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["bank_id", "account_code"], name="unique_bank_account_code"
            )
        ]

    def __str__(self):
        return str(self.account_code)


class Transaction(models.Model):
    TYPE_CHOICES = [
        ("income", "Доход"),
        ("expense", "Расход"),
    ]

    INCOME_SUBTYPE_CHOICES = [
        ("salary", "Зарплата"),
        ("gift", "Подарок"),
        ("investment", "Инвестиции"),
        ("transfer", "Перевод"),
    ]

    EXPENSE_SUBTYPE_CHOICES = [
        ("entertainment", "Развлечения"),
        ("food", "Еда"),
        ("transport", "Транспорт"),
        ("utilities", "Коммунальные услуги"),
        ("transfer", "Перевод"),
    ]

    account_id = models.ForeignKey("Account", on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    subtype = models.CharField(max_length=30, null=True)
    date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.type == "income" and self.subtype not in dict(
            self.INCOME_SUBTYPE_CHOICES
        ):
            raise ValueError("Invalid subtype for income")
        elif self.type == "expense" and self.subtype not in dict(
            self.EXPENSE_SUBTYPE_CHOICES
        ):
            raise ValueError("Invalid subtype for expense")
        super().save(*args, **kwargs)

    def get_subtype_choices(self):
        if self.type == "income":
            return self.INCOME_SUBTYPE_CHOICES
        elif self.type == "expense":
            return self.EXPENSE_SUBTYPE_CHOICES
        return []


class UserAccount(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    date = models.DateField(null=True)


class PeriodicPayment(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    period_type = models.CharField(max_length=100)
    period = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
    creator = models.CharField(max_length=255, default="")
