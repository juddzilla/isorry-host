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

        representation['reason'] = instance.reason[:140]

        return representation