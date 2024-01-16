from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from apology.models import Apology
from django.core.exceptions import ValidationError
from .models import Completions

class CompletionApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, apology_uuid, user_id):
        '''
        Helper method to get the object with given apology_id, and user_id
        '''            
        def get_apology(apology_uuid, user_id):
            try:
                return Apology.objects.get(uuid=apology_uuid, user_id=user_id)       
            except (Apology.DoesNotExist, ValidationError):
                return None
        
        apology = get_apology(apology_uuid, user_id)                
        if not apology:
             return None
        try:            
            completion = Completions.objects.get(apology_id=apology.id)
            return completion
        except Completions.DoesNotExist:
            return None
    
    def get(self, request, apology_uuid, *args, **kwargs):        
        '''
        Retrieves the Completion with given apology_uuid
        '''        
        completion = self.get_object(apology_uuid, request.user.id)
        if not completion:
            return Response(
                {"error": "Apology Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        response = {
            "created_at": completion.created_at.strftime("%A %B %d, %Y %l:%M %p"),
            "message": completion.message,      
            "model": completion.model,      
            "reason": completion.apology.reason,
        }
                
        return Response(response, status=status.HTTP_200_OK)

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