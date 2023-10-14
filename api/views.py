from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Hangman
from .serializers import Hangmanserializer
from rest_framework import permissions

class HangmanApiView(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Hangman.objects.all()
    serializer_class = Hangmanserializer

class HangmanApiCreate(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Hangman.objects.all()
    serializer_class = Hangmanserializer

class HangmanApiUpdate(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Hangman.objects.all()
    serializer_class = Hangmanserializer