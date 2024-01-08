from django.urls import path
from .views import (
    ApologyDetailApiView
)

urlpatterns = [
    path('<slug:apology_uuid>/', ApologyDetailApiView.as_view()),
]