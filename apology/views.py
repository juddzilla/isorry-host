from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Apology
from .serializers import ApologySerializer
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
        def apply(a):                
            return {                    
                'created_at': a.created_at.strftime("%A %B %d, %Y %l:%M %p"),
                'reason': a.reason[:80],
                'type': a.type,
                'uuid': str(a.uuid),
            }

        apologies = Apology.objects.filter(user=request.user.id)
        mapped = map(apply, apologies)
        return Response(list(mapped), status=status.HTTP_200_OK)


class ApologyView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Create the Apology with given apology data
        '''        
        print(request.user.id)
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
            completion = Request(apology.id, messages)
            
            if hasattr(completion, 'id'):
                return Response({
                    "created_at": completion.created_at.strftime("%A %B %d, %Y %l:%M %p"),
                    "message": completion.message,
                    "model": completion.model,
                    "reason": apology.reason,
                    "uuid": apology.uuid,
                }, status=status.HTTP_201_CREATED)        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
