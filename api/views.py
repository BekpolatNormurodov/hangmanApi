from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = [
        {'question':'kitob', 'answer': 'book'},
        {'question':'olma', 'answer': 'apple'},
        {'question':'ism', 'answer': 'name'},
        {'question':'yosh', 'answer': 'age'},
        {'question':'salom', 'answer': 'hello'},
        {'question':'yordam', 'answer': 'help'},
        {'question':'inson', 'answer': 'person'},
        {'question':'rasm', 'answer': 'picture'},
        {'question':'ruchka', 'answer': 'per'},
        {'question':'qizil', 'answer': 'red'},
    ]
    return Response(person)