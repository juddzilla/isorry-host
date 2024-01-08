from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apology.models import Apology
from .models import Completions
from .serializers import CompletionsSerializer
from completions.request import Request
# Create your views here.

class ApologyDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, apology_uuid):
        '''
        Helper method to get the object with given apology_id, and user_id
        '''
        
        try:
            apology = Apology.objects.get(uuid=apology_uuid)            
            completion = Completions.objects.get(apology_id=apology.id)
            return CompletionsSerializer(completion)
        except Apology.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, apology_uuid, *args, **kwargs):        
        '''
        Retrieves the Apology with given apology_id
        '''
        apology_completion = self.get_object(apology_uuid)        
        if not apology_completion:
            return Response(
                {"res": "Object with apology id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        response = {
            "created_at": apology_completion.data['created_at'],
            "message": apology_completion.data['message'],
        }
                
        return Response(response, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, apology_uuid, *args, **kwargs):
        '''
        Updates the apology with given apology_id if exists
        '''
        apology_instance = self.get_object(apology_uuid, request.user.id)
        if not apology_instance:
            return Response(
                {"res": "Object with apology id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'reason': request.data.get('reason'), 
            'type': request.data.get('type'), 
            'parameters': request.data.get('parameters'), 
            'user': request.user.id
        }
        serializer = ApologySerializer(instance = apology_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, apology_uuid, *args, **kwargs):
        '''
        Deletes the apology item with given apology_id if exists
        '''
        apology_instance = self.get_object(apology_uuid, request.user.id)
        if not apology_instance:
            return Response(
                {"res": "Object with apology id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        apology_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )