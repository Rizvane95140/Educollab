from django.db import models
from account.models import Account
from topic.models import Topics

# Create your models here.

class Messages(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)    
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['user', 'topic', 'message']

    def __str__(self):
        return self.message