from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Apology
from .serializers import ApologySerializer, ApologiesSerializer
from completions.serializers import CompletionPublicSerializer
import uuid
from .messages import Messages
from completions.request import Request
from datetime import datetime
        
class ApologiesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the apologies for given requested user
        '''
  
        apologies = Apology.objects.filter(user=request.user.id)  
        serialized = ApologiesSerializer(apologies, many=True)    
        return Response(serialized.data, status=status.HTTP_200_OK)


class ApologyView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Create the Apology with given apology data
        '''        
        data = {
            'reason': request.data.get('reason'), 
            'type': request.data.get('type'), 
            'parameters': request.data.get('parameters'), 
            'user': request.user.id,
            'uuid': uuid.uuid4()
        }
        serializer = ApologySerializer(data=data)
        
        if serializer.is_valid():
            apology = serializer.save()            
            
            messages = Messages(request.data.get('reason'), request.data.get('type'), request.data.get('parameters'))
            completion = Request(messages)
            
            apology_serialized = ApologiesSerializer(apology)
            completion_serialized = CompletionPublicSerializer(apology.completion)
            if completion is not None:
                apology.completion = completion
                apology.save()
                return Response({
                   **apology_serialized.data,
                   **completion_serialized.data
                }, status=status.HTTP_201_CREATED)        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
