from django.urls import path
from .views import (ApologyListApiView)

urlpatterns = [
    path('', ApologyListApiView.as_view()),
]