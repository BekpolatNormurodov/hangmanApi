from rest_framework.generics import ListAPIView
from api.models import Hangman
from .serializers import Hangmanserializer

class HangmanApiView(ListAPIView):
    queryset = Hangman.objects.all()
    serializer_class = Hangmanserializer