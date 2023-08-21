from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = [
        {'question':'olmalar', 'answer': 'apples'},
    ]
    return Response(person)