from django.db import models

class BalanceSheet(models.Model):
    cash                = models.DecimalField(max_digits=15, decimal_places=6)
    current_liabilities = models.DecimalField(max_digits=15, decimal_places=6)
