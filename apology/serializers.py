from rest_framework import serializers
from .models import Apology

class ApologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apology
        fields = ["parameters", "reason", "type", "created_at", "updated_at", "user", "uuid"] 
