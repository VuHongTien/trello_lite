from django.urls import path
from .apis import *

urlpatterns = [
    path('create', TaskCreateApi.as_view(), name='create_task'),
    path('<int:task_id>', TaskDetailApi.as_view(), name='task_detail'),
    path('<int:task_id>/update', TaskUpdateApi.as_view(), name='update_task'),
    path('<int:task_id>/delete', TaskDeleteApi.as_view(), name='delete_task'),
]
