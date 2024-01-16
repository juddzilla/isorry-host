from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the sessionid from the request cookies
        # sessionid = request.COOKIES.get('sessionid')
        sessionid = request.COOKIES.get('sessionid')            
        print(request.COOKIES)
        # Check if sessionid exists
        if sessionid:
            try:
                # Find the user associated with the sessionid
                session = Session.objects.get(session_key=sessionid)
                user_id = session.get_decoded().get('_auth_user_id')  
                user = User.objects.get(id=user_id)
                # Attach the user to the request for easy access in views
                print(500)
                print(user)
                request.user = user
            except (Session.DoesNotExist, User.DoesNotExist):
                print(700)
                pass

        response = self.get_response(request)
        return response
