from django.urls import path
from .views import (
    ApologyListApiView,
    ApologyDetailApiView
)

urlpatterns = [
    path('', ApologyListApiView.as_view()),
    path('<slug:apology_uuid>/', ApologyDetailApiView.as_view()),
]