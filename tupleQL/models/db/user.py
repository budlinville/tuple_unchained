from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSecrets(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    alpha_vantage_key=models.CharField(max_length=20)
