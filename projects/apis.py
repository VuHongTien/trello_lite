from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.conf import settings

from utils.serializer_validator import validate_serializer
from .models import Project
from .services import *
from utils.exceptions import *
from projects.permissions import *


class ProjectCreateApi(APIView):
    permission_classes = [UserPermission, ]

    class RequestSerializer(serializers.Serializer):
        title = serializers.CharField(required=True, max_length=255)
        description = serializers.CharField(required=True, max_length=255)

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = '__all__'

    def post(self, request):
        self.check_permissions(request=request)
        request_serializer = self.RequestSerializer(data=request.data)
        validate_serializer(serializer=request_serializer)
        project = create_project(user=request.user, **request_serializer.validated_data)
        response_serializer = self.ResponseSerializer(project)
        return Response({
            'project': response_serializer.data
        }, status=status.HTTP_200_OK)


class ProjectJoinApi(APIView):
    permission_classes = [UserPermission, ]

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = '__all__'

    def post(self, request, project_id):
        self.check_permissions(request=request)
        project = get_projects_by(id=project_id).first()
        project = join_project(user_id=request.user.id, project=project)
        response_serializer = self.ResponseSerializer(project)
        return Response({
            'project': response_serializer.data
        }, status=status.HTTP_200_OK)


class ProjectDetailApi(APIView):
    permission_classes = [UserPermission, ]

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = '__all__'

    def get(self, request, project_id):
        self.check_permissions(request=request)
        project = get_projects_by(id=project_id).first()
        response_serializer = self.ResponseSerializer(project)
        return Response({
            'project': response_serializer.data
        }, status=status.HTTP_200_OK)


class ProjectListApi(APIView):
    permission_classes = [UserPermission, ]

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = '__all__'

    def get(self, request):
        self.check_permissions(request=request)
        projects = list(get_projects_by())
        response_serializer = self.ResponseSerializer(projects, many=True)
        return Response({
            'projects': response_serializer.data
        }, status=status.HTTP_200_OK)
