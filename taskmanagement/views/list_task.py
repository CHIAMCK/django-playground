
from django.views.generic import ListView

from taskmanagement.models import Task
from taskmanagement.tables import TaskTable
from django_tables2.views import SingleTableMixin


class ListTaskView(SingleTableMixin, ListView):
    # ListView
    model = Task

    # django table
    table_class = TaskTable
