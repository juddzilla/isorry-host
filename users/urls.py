from django.urls import path
from .views import (UserAuthCheck, UserLogoutView)

urlpatterns = [
    path('logout', UserLogoutView.as_view()),
    path('check', UserAuthCheck.as_view()),
]