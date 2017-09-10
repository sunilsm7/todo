from rest_framework.views import APIView
from rest_framework.response import Response

from todo.models import ToDo
from todo.serializers import ToDoSerializer

class ToDoView(APIView):
		def get(self, request):
    			todos	= ToDo.objects.all()
    			serializer = ToDoSerializer(todos, many=True)
    			return Response(serializer.data)
