from django.urls import path
from .apis import *

urlpatterns = [
    path('create', ProjectCreateApi.as_view(), name='project_create'),
    path('<int:project_id>', ProjectDetailApi.as_view(), name='project_detail'),
    path('<int:project_id>/join', ProjectJoinApi.as_view(), name='project_join'),
    path('', ProjectListApi.as_view(), name='project_list'),
]
