from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Apology
from .serializers import ApologySerializer
# from rest_framework import permissions
import uuid
from .ai import AI
from .messages import Messages
from completions.request import Request
        
class ApologyListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]
    
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the apologies for given requested user
        '''
        apologies = Apology.objects.filter(user = request.user.id)
        serializer = ApologySerializer(apologies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Apology with given apology data
        '''        
        apology_uuid = uuid.uuid4()
        data = {
            'reason': request.data.get('reason'), 
            'type': request.data.get('type'), 
            'parameters': request.data.get('parameters'), 
            'user': request.user.id,
            'uuid': apology_uuid
        }
        serializer = ApologySerializer(data=data)
        
        if serializer.is_valid():
            apology = serializer.save()            
            
            messages = Messages(request.data.get('reason'), request.data.get('type'), request.data.get('parameters'))
            completion = Request(apology.id, messages)
            
            if hasattr(completion, 'id'):
                return Response({
                    "message": completion.message,
                    "uuid": apology.uuid,
                }, status=status.HTTP_201_CREATED)        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
