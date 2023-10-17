from django.urls import path
from .views import HangmanApiView, HangmanApiCreate, HangmanApiUpdate

urlpatterns = [
    path('',HangmanApiView.as_view()),
    path('add/',HangmanApiCreate.as_view()),
    path('<int:pk>',HangmanApiUpdate.as_view()),
]