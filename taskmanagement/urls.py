from django.urls import path
import taskmanagement.views

app_name = 'tasks'

urlpatterns = [
    path('add', taskmanagement.views.AddTaskView.as_view(), name='add'),
    path('list', taskmanagement.views.ListTaskView.as_view(), name='list'),
]
