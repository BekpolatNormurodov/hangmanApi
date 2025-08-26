from rest_framework.views import APIView
from rest_framework.response import Response
import random


class CrosswordAPI(APIView):
    def get(self, request):
        name = []
        return Response(name) 