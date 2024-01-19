from django.urls import path
from .views import (GithubOAuthView, GoogleOAuthView)

urlpatterns = [
    path('google', GoogleOAuthView.as_view()),
    path('github', GithubOAuthView.as_view()),
]