from django.db import models
from django.contrib.auth.models import User

class Apology(models.Model):
    parameters = models.JSONField()
    reason = models.TextField()
    type = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.reason