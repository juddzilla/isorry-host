from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
import requests
import os

def find_user(username):
    try:
        return User.objects.get(username=username)
    except ObjectDoesNotExist:
       return None
    
def create_user(data):
    return User.objects.create_user(username=data['username'],email=data['email'],first_name=data['first_name'],last_name=data['last_name'])            

def user_login(request, user):
    login(request, user, backend='django.contrib.auth.backends.BaseBackend')

class GoogleOAuthView(APIView):    
    def get(self, request, *args, **kwargs):        
        token = request.GET.get('token')
        url = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json'
        req = requests.get(
            url, 
            headers = {'Authorization': f'Bearer {token}'})
        req_user = req.json()
        username = f'google:{req_user['id']}'        
        user = find_user(username=username)

        if user is None:
            user = create_user({'email': req_user['email'], 'first_name': req_user['given_name'], 'last_name': req_user['family_name'], 'username': username})

        user_login(request, user)                                        
        
        return Response({ "success": 100 }, status=status.HTTP_200_OK)


class GithubOAuthView(APIView):
    def get_token(self, code):        
        req = requests.post(
            'https://github.com/login/oauth/access_token',
            data={
                'client_id': os.environ["GITHUB_CLIENT_ID"],
                'client_secret':os.environ["GITHUB_SECRET"], 
                'code': code,
                'scope': 'read:user'
            }, 
            headers={'Accept': 'application/json'})        
        return req.json()
    
    def get_user(self, token):        
        req_user = requests.get(
            'https://api.github.com/user',
            headers = {'Authorization': f'Bearer {token}'})        
        user = req_user.json()              
        first, *last = user['name'].split()
        return {
            "email": user['email'],
            "first_name": first,
            "last_name": " ".join(last),
            "username": f'github:{user['id']}'
        }

    def get(self, request, *args, **kwargs):                
        code = request.GET.get('code')
        token = self.get_token(code) 
        token_user = self.get_user(token['access_token'])                
        user = find_user(username=token_user['username'])

        if user is None:
            user = create_user(token_user)

        user_login(request, user)
        return Response({'success': 100 }, status=status.HTTP_200_OK)

