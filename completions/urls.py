from django.urls import path
from .views import (
    CompletionApiView
)

urlpatterns = [
    path('<slug:apology_uuid>/', CompletionApiView.as_view()),
]