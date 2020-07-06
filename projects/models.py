from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from django.conf import settings

from .managers import ProjectManager
from users.models import User


class Project(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    admin = models.ForeignKey(User, related_name='own_projects', on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProjectManager()

    class Meta:
        app_label = 'projects'
        db_table = 'project'

    def __str__(self):
        return self.title
