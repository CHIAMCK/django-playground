from rest_framework.generics import ListAPIView
from ..serializers import TaskSerializer
from taskmanagement.models import Task
from taskmanagement.views.mixins import RestrictTaskListMixin


class TaskListView(RestrictTaskListMixin, ListAPIView):
    # override the get_queryset method to get tasks belong to user
    # .all() will call the get_queryset method
    queryset = Task.objects.all().order_by('-created_date')
    serializer_class = TaskSerializer
