from django.urls import path
from .views import HangmanApiView

urlpatterns = [
    path('',HangmanApiView.as_view()),
]