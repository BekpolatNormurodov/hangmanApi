from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = [
        {'question':'oq', 'answer': 'white'},
        {'question':'qizil', 'answer': 'red'},
        {'question':'sariq', 'answer': 'yellow'},
        {'question':'kok', 'answer': 'blue'},
        {'question':'yashil', 'answer': 'green'},
        {'question':'qora', 'answer': 'black'},
    ]
    return Response(person)