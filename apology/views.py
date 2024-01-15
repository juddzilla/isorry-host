from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Apology
from .serializers import ApologySerializer
import uuid
from .messages import Messages
from completions.request import Request

        
class ApologyListApiView(APIView):
        
    def get(self, request, *args, **kwargs):
        '''
        List all the apologies for given requested user
        '''
        if not request.user.id:
            return Response(
                {"res": "User does not have any apologies"},
                status=status.HTTP_404_NOT_FOUND
            )
        apologies = Apology.objects.filter(user = request.user.id)
        serializer = ApologySerializer(apologies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
            completion = Request(apology.id, messages)
            
            if hasattr(completion, 'id'):
                return Response({
                    "message": completion.message,
                    "uuid": apology.uuid,
                }, status=status.HTTP_201_CREATED)        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
