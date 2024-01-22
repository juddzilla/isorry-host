from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from apology.models import Apology
from django.core.exceptions import ValidationError
from .models import Completions
from .serializers import CompletionPublicSerializer
from apology.serializers import ApologiesSerializer

class CompletionApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_apology(self, apology_uuid, user_id):
            try:
                return Apology.objects.get(uuid=apology_uuid, user_id=user_id)       
            except (Apology.DoesNotExist, ValidationError):
                return None

    
    def get(self, request, apology_uuid, *args, **kwargs):        
        '''
        Retrieves the Completion with given apology_uuid
        '''        
        apology = self.get_apology(apology_uuid, request.user.id)       
        
        if any(value is None for value in [apology, apology.completion]):
            return Response({
                    "error": "Apology Not Found"
                 },
                status=status.HTTP_404_NOT_FOUND
            )
                
        completion_serialized = CompletionPublicSerializer(apology.completion)
        apology_serialized = ApologiesSerializer(apology)
        
        return Response({
                **completion_serialized.data,
                **apology_serialized.data,
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request, apology_uuid, *args, **kwargs):
        '''
        Deletes the Completion item with given apology_uuid if exists
        '''
        completion = self.get_object(apology_uuid, request.user.id)
        if not completion:
            return Response(
                {"error": "Apology not deleted"},
                status=status.HTTP_404_NOT_FOUND
            )
        completion.delete()

        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )