from django.urls import path
from .views import (ApologyView, ApologiesView)

urlpatterns = [
    path('', ApologyView.as_view()),
    path('list', ApologiesView.as_view()),
]