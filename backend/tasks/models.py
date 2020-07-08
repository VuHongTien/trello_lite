from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from django.conf import settings

from .managers import TaskManager
from projects.models import Project


class Task(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    UN_DONE = 0
    IN_PROGRESS = 1
    COMPLETED = 2

    TASK_TYPES_CHOICES = (
        (UN_DONE, 'UN_DONE'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (COMPLETED, 'COMPLETED'),
    )

    detail = models.CharField(max_length=settings.CHARFIELD_LENGTH, unique=True)
    status = models.SmallIntegerField(choices=TASK_TYPES_CHOICES, default=0)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.SET_NULL, null=True)

    objects = TaskManager()

    class Meta:
        app_label = 'tasks'
        db_table = 'task'

    def __str__(self):
        return self.detail
