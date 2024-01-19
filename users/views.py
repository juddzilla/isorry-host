from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

class UserLogoutView(APIView):    
    def get(self, request, *args, **kwargs):        
        response = Response({ "success": 100 }, status=status.HTTP_200_OK)
        response.delete_cookie('sessionid')
        return response

class UserAuthCheck(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return Response({"check": 100}, status=status.HTTP_200_OK)