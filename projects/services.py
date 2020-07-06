from .models import Project

from utils.exceptions import ObjectNotFound
from users.services import get_user_by


def get_projects_by(with_deleted=False, raise_exception=True, **kwargs):
    projects = Project.objects.all_with_deleted().filter(**kwargs) if with_deleted else Project.objects.all().filter(
        **kwargs)
    if not projects and not raise_exception:
        raise ObjectNotFound
    return projects


def create_project(user, **kwargs):
    project = Project.objects.create(admin=user, **kwargs)
    return project


def join_project(user_id, project):
    user = get_user_by(id=user_id)
    project.users.add(user)
    project.save()
    return project
