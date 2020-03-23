from django.db import models
from django.contrib.auth import get_user_model


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='links',
        null=True,
        blank=True,
    )
