
from django.db import models


class Task(models.Model):

    # a fixed length string (can contain letters, numbers and special characters)
    # size can be from 0 to 255, default is 1
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True, default='')

    assigned_to = models.ManyToManyField(
        to='auth.User',
        related_name='assigned_to_tasks'
    )

    created_by = models.ForeignKey(
        to='auth.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    updated_by = models.ForeignKey(
        to='auth.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    deleted_by = models.ForeignKey(
        to='auth.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
