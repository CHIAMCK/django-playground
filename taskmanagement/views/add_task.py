from django.views.generic.edit import CreateView
from taskmanagement.models import Task
from taskmanagement.forms import AddTaskForm


class AddTaskView(CreateView):
    model = Task
    form_class = AddTaskForm
