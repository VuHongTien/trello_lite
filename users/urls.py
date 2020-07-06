from django.urls import path
from .apis import *

urlpatterns = [
    path('sign_in', UserSignInApi.as_view(), name='sign_in'),
    path('sign_up', UserSignUpApi.as_view(), name='sign_up'),
    path('<int:user_id>', UserDetailApi.as_view(), name='user_detail'),
    path('<int:user_id>/update', UserUpdateApi.as_view(), name='user_update'),
    path('<int:user_id>/change_password', UserChangePasswordApi.as_view(), name='user_change_password'),
    path('<int:user_id>/projects', UserListProjectsApi.as_view(), name='user_list_projects')
]
