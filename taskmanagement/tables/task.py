
import django_tables2 as tables

from taskmanagement.models.task import Task


class TaskTable(tables.Table):

    title = tables.Column(
        'Title', orderable=False,
    )

    description = tables.Column(
        'Description', orderable=False
    )

    created_by = tables.Column(
        'Created By', orderable=False
    )

    class Meta():
        model = Task
        # add custom HTML attributes to the table
        attrs = {'class': 'table table-striped table-responsive-sm'}
        fields = (
            'title', 'description', 'created_by'
        )
