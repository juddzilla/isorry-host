from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from apology.models import Apology
from .models import Completions
from .serializers import CompletionsSerializer

def get_apology(apology_uuid, user_id):
    try:
        return Apology.objects.get(uuid=apology_uuid, user_id=user_id)       
    except Apology.DoesNotExist:
        return None

class CompletionApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, apology_uuid, user_id):
        '''
        Helper method to get the object with given apology_id, and user_id
        '''                
        apology = get_apology(apology_uuid, user_id)        
        if not apology:
             return None
        try:            
            completion = Completions.objects.get(apology_id=apology.id)
            return CompletionsSerializer(completion)
        except Completions.DoesNotExist:
            return None
    
    def get(self, request, apology_uuid, *args, **kwargs):        
        '''
        Retrieves the Completion with given apology_uuid
        '''        
        completion = self.get_object(apology_uuid, request.user.id)
        if not completion:
            return Response(
                {"res": "Object with apology id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        response = {
            "created_at": completion.data['created_at'],
            "message": completion.data['message'],
        }
                
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, apology_uuid, *args, **kwargs):
        '''
        Deletes the Completion item with given apology_uuid if exists
        '''
        completion = self.get_object(apology_uuid, request.user.id)
        if not completion:
            return Response(
                {"res": "Object with apology id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        completion.delete()

        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )