from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.conf import settings

from utils.serializer_validator import validate_serializer
from .models import Task
from .services import *
from utils.exceptions import *
from tasks.permissions import *


class TaskCreateApi(APIView):
    permission_classes = [UserPermission, ]

    class RequestSerializer(serializers.Serializer):
        detail = serializers.CharField(required=True, max_length=255)
        project_id = serializers.IntegerField(required=True)

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = '__all__'

    def post(self, request):
        self.check_permissions(request=request)
        request_serializer = self.RequestSerializer(data=request.data)
        validate_serializer(serializer=request_serializer)
        task = create_task(**request_serializer.validated_data)
        response_serializer = self.ResponseSerializer(task)
        return Response({
            'task': response_serializer.data
        }, status=status.HTTP_200_OK)


class TaskDetailApi(APIView):
    permission_classes = [UserPermission, ]

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = '__all__'

    def get(self, request, task_id):
        task = get_tasks_by(id=task_id).first()
        self.check_object_permissions(request=request, obj=task)
        response_serializer = self.ResponseSerializer(task)
        return Response({
            'task': response_serializer.data
        }, status=status.HTTP_200_OK)


class TaskUpdateApi(APIView):
    permission_classes = [UserPermission, ]

    class RequestSerializer(serializers.Serializer):
        detail = serializers.CharField(required=True)
        status = serializers.IntegerField(required=True)

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = '__all__'

    def put(self, request, task_id):
        request_serializer = self.RequestSerializer(data=request.data)
        validate_serializer(serializer=request_serializer)
        task = get_tasks_by(id=task_id).first()
        task = update_task(task=task, detail=request_serializer.validated_data['detail'],
                           status=request_serializer.validated_data['status'])
        self.check_object_permissions(request=request, obj=task)
        response_serializer = self.ResponseSerializer(task)
        return Response({
            'task': response_serializer.data
        }, status=status.HTTP_200_OK)


class TaskDeleteApi(APIView):
    permission_classes = [UserPermission, ]

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = '__all__'

    def delete(self, request, task_id):
        task = get_tasks_by(id=task_id).first()
        self.check_object_permissions(request=request, obj=task)
        task = delete_task(task=task)
        response_serializer = self.ResponseSerializer(task)
        return Response({
            'task': response_serializer.data
        }, status=status.HTTP_200_OK)
