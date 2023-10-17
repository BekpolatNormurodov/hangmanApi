from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Hangman
from .serializers import Hangmanserializer

class HangmanApiView(ListAPIView):
    queryset = Hangman.objects.all()
    serializer_class = Hangmanserializer

class HangmanApiCreate(ListCreateAPIView):
    queryset = Hangman.objects.all()
    serializer_class = Hangmanserializer

class HangmanApiUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Hangman.objects.all()
    serializer_class = Hangmanserializer