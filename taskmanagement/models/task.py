
from django.db import models
from taskmanagement.tasks import send_verification_email


class Task(models.Model):

    # a fixed length string (can contain letters, numbers and special characters)
    # size can be from 0 to 255, default is 1
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True, default='')

    assigned_to = models.ManyToManyField(
        to='auth.User',
        related_name='assigned_to_tasks'
    )

    board = models.ForeignKey(
        to='board.Board',
        null=True,
        on_delete=models.SET_NULL,
        related_name='board_tasks'
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
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    deleted_by = models.ForeignKey(
        to='auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)

    def save(self, commit=True):
        send_verification_email.delay('123', '321', '123@gmail.com', ['809@gmail.com'], True)
        return super().save(commit)
