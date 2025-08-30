from rest_framework.views import APIView
from rest_framework.response import Response
import random


class CrosswordAPI(APIView):
    def get(self, request):

        lst_1 = [
            {
                "question": "Jon kuydurmasang, .... qayda, \nToqqa chiqmasang, do'lana qayda."
                "answer"  : "janona"
            },
            {
                "question": "Besh barmoq .... emas."
                "answer"  : "barobar"
            },
            {
                "question": ""
                "answer"  : ""
            },
            {
                "question": ""
                "answer"  : ""
            },
            {
                "question": ""
                "answer"  : ""
            },
            {
                "question": ""
                "answer"  : ""
            },
            {
                "question": ""
                "answer"  : ""
            },
            {
                "question": ""
                "answer"  : ""
            },
            {
                "question": ""
                "answer"  : ""
            },
            {
                "question": ""
                "answer"  : ""
            },
        ]

        return Response(name) 