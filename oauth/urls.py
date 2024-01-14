from django.urls import path
from .views import (GoogleOAuthView)

urlpatterns = [
    path('', GoogleOAuthView.as_view()),
]