from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
import requests

class GoogleOAuthView(APIView):    
    def get(self, request, *args, **kwargs):        
        token = request.GET.get('token')
        url = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json'
        req = requests.get(url, headers = {'Authorization': f'Bearer {token}'})
        # req.json() = {'id': '100', 'email': 'email@email.com', 'verified_email': True, 'name': 'First Last', 'given_name': 'First', 'family_name': 'Last', 'picture': 'https://lh3.googleusercontent.com/a/asdfsdfaf', 'locale': 'en'}
        req_user = req.json()
        try:
            user = User.objects.get(email=req_user['email'])
            login(request, user, backend='django.contrib.auth.backends.BaseBackend')                                        
        except ObjectDoesNotExist:        
            user = User.objects.create_user(req_user['email'],email=req_user['email'],first_name=req_user["given_name"],last_name=req_user["family_name"])            

        return Response({ "success": 100 }, status=status.HTTP_200_OK)

