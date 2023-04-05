from django.db import models

class BalanceSheet(models.Model):
    ticker              = models.CharField(max_length=10)
    cash                = models.DecimalField(max_digits=15, decimal_places=6)
    accounts_receivable = models.DecimalField(max_digits=15, decimal_places=6)
    current_liabilities = models.DecimalField(max_digits=15, decimal_places=6)
