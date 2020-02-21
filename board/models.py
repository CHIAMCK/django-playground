from django.db import models


class Board(models.Model):

    name = models.CharField(
        max_length=200,
    )

    user = models.ForeignKey(
        to='auth.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_boards',
    )
