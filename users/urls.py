from django.urls import path
from .views import (UserLogoutView)

urlpatterns = [
    path('', UserLogoutView.as_view()),
]