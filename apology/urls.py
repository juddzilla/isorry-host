from django.urls import path
from .views import (
    ApologyListApiView,
    ApologyDetailApiView
)

urlpatterns = [
    path('', ApologyListApiView.as_view()),
    path('<int:apology_id>/', ApologyDetailApiView.as_view()),
]