from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


from ..models import Task
from .serializers import TaskSerializer

@api_view()
def task_api_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(instance=tasks, many=True)
    return Response(serializer.data)

@api_view()
def task_api_detail(request,pk):
    task = get_object_or_404(
        Task.objects.all(),pk=pk
    )
    serializer = TaskSerializer(instance=task, many=False)
    return Response(serializer.data)    


    #!EXEMPLO DE UTILIZAÇÃO DO GET_OBJECT_OR_404
    #? task = Task.objects.all().filter(pk=pk).first()

    #? if task:
    #?     serializer = TaskSerializer(instance=task, many=False)
    #?     return Response(serializer.data)

    #? else:
    #?     return Response({"error" : "Task not found"}, status=status.HTTP_404_NOT_FOUND)
