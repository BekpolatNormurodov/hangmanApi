# from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .serializers import Hangmanserializer
# from api.models import Hangman
from rest_framework.views import APIView
from rest_framework.response import Response


# class HangmanApiView(ListAPIView):
#     queryset = Hangman.objects.all()
#     serializer_class = Hangmanserializer

# class HangmanApiCreate(ListCreateAPIView):
#     queryset = Hangman.objects.all()
#     serializer_class = Hangmanserializer

# class HangmanApiUpdate(RetrieveUpdateDestroyAPIView):
#     queryset = Hangman.objects.all()
#     serializer_class = Hangmanserializer

class HangmanApiView(APIView):
    def get(self, request):
        phones = []
        return Response(phones)