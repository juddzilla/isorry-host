from rest_framework import serializers
from .models import Apology

class ApologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apology
        fields = ["parameters", "reason", "type", "created_at", "updated_at", "user", "uuid", "completion"] 

class ApologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apology
        fields = [ "reason", "type", "created_at", "uuid"]         

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['created_at'] = instance.created_at.strftime("%A %B %d, %Y %l:%M %p")

        return representation