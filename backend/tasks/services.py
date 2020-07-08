from tasks.models import Task
from projects.services import Project
from projects.services import get_projects_by

from utils.exceptions import *


def get_tasks_by(with_deleted=False, raise_exception=True, **kwargs):
    tasks = Task.objects.all_with_deleted().filter(**kwargs) if with_deleted else Task.objects.all().filter(
        **kwargs)
    if not tasks and not raise_exception:
        raise ObjectNotFound
    return tasks


def create_task(project_id, detail):
    project = get_projects_by(id=project_id).first()
    task = Task(project=project, detail=detail)
    task.save()
    return task


def update_task(task, detail, status):
    task.detail = detail
    task.status = status
    task.save()
    return task


def delete_task(task):
    task.delete()
    return task
