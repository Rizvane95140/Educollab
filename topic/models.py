from django.db import models
from account.models import Account
# Create your models here.

class Topics(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['user', 'title']

    def __str__(self):
        return self.title