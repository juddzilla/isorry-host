from rest_framework import serializers
from .models import Completions

class CompletionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completions
        fields = [
            "ai_created_at",
            "ai_id",
            "apology",
            "completion_tokens",
            "created_at",
            "message",
            "messages",            
            "model",
            "prompt_tokens",
        ] 
