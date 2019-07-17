from rest_framework.generics import ListAPIView

from taskmanagement.models import Task

from ..serializers import TaskSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # override get queryset method to return tasks that are assigned to the user
    def get_queryset(self):
        user = self.request.user
        qs = Task.objects.filter(
            assigned_to=user.id
        )
        return qs
