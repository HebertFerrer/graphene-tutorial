from django.db import models
from django.contrib.auth import get_user_model


class Vote(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='votes',
    )
    link = models.ForeignKey(
        'links.Link',
        on_delete=models.CASCADE,
        related_name='votes',
    )
    created = models.DateTimeField(auto_now_add=True)
