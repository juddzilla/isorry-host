from django.db import models

class Completions(models.Model):
    ai_created_at = models.DateTimeField()
    ai_id = models.TextField(unique=True)    
    completion_tokens = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)    
    message = models.TextField()
    messages = models.JSONField()
    model = models.TextField()
    prompt_tokens = models.IntegerField()    