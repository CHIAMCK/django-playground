
from django.views.generic import ListView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from taskmanagement.filters import TaskFilter
from taskmanagement.models import Task
from taskmanagement.tables import TaskTable


class ListTaskView(SingleTableMixin, FilterView):
    # ListView
    model = Task

    # django table
    table_class = TaskTable

    template_name_suffix = '_list'

    # django filter
    filterset_class = TaskFilter
