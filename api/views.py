from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = [
        {'name':'Dennis', 'age':28},
        {'name':'Jhon', 'age':20},
        {'name':'Dennis', 'age':28},
        {'name':'Jhon', 'age':20},
        {'name':'Dennis', 'age':28},
        {'name':'Jhon', 'age':20},
        {'name':'Dennis', 'age':28},
        {'name':'Jhon', 'age':20},
    ]
    return Response(person)