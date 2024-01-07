# from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Apology
from .serializers import ApologySerializer
from rest_framework import permissions
import uuid
from .ai import AI
from .messages import Messages
from completions.request import Request
        
class ApologyListApiView(APIView):
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
                    "uuid": apology_uuid,
                }, status=status.HTTP_201_CREATED)        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApologyDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, apology_uuid, user_id):
        '''
        Helper method to get the object with given apology_id, and user_id
        '''
        try:
            return Apology.objects.get(uuid=apology_uuid, user = user_id)
        except Apology.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, apology_uuid, *args, **kwargs):
        '''
        Retrieves the Apology with given apology_id
        '''
        apology_instance = self.get_object(apology_uuid)
        if not apology_instance:
            return Response(
                {"res": "Object with apology id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ApologySerializer(apology_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
