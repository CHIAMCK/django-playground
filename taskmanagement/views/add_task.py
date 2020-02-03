from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from taskmanagement.models import Task
from taskmanagement.forms import AddTaskForm


class AddTaskView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = AddTaskForm
    success_url = reverse_lazy('dashboard:main')
    # django message
    success_message = 'Task "%(title)s" was created successfully'
