from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.conf import settings

from users.permissions import *
from .services import *
from .models import User
from auth_tokens.services import create_token
from utils.serializer_validator import validate_serializer
from projects.models import Project
from projects.services import get_projects_by


class UserSignInApi(APIView):
    permission_classes = [AllowAny, ]

    class RequestSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True, max_length=settings.CHARFIELD_LENGTH)
        password = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'name', 'email', 'tel']

    def post(self, request):
        request_serializer = self.RequestSerializer(data=request.data)
        validate_serializer(serializer=request_serializer)
        user = authenticate_user(**request_serializer.validated_data)
        token = create_token(user)
        response_serializer = self.ResponseSerializer(user)
        return Response({
            'user': response_serializer.data,
            'token': token
        }, status=status.HTTP_200_OK)


class UserSignUpApi(APIView):
    permission_classes = [AllowAny, ]

    class RequestSerializer(serializers.Serializer):
        email = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)
        name = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)
        tel = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)
        password = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)
        password_confirm = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'name', 'email', 'tel']

    def post(self, request):
        request_serializer = self.RequestSerializer(data=request.data)
        validate_serializer(serializer=request_serializer)
        user = create_user(**request_serializer.validated_data)
        response_serializer = self.ResponseSerializer(user)
        return Response({
            'user': response_serializer.data
        }, status=status.HTTP_201_CREATED)


class UserDetailApi(APIView):
    permission_classes = [UserPermission, ]

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'name', 'email', 'tel']

    def get(self, request, user_id):
        user = get_user_by(id=user_id)
        self.check_object_permissions(request, obj=user)
        serializer = self.ResponseSerializer(user)
        return Response({
            'user': serializer.data
        }, status=status.HTTP_200_OK)


class UserUpdateApi(APIView):
    permission_classes = [UserPermission, ]

    class RequestSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        tel = serializers.CharField(max_length=255)

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'name', 'email', 'tel']

    def put(self, request):
        request_serializer = self.RequestSerializer(data=request.data)
        validate_serializer(serializer=request_serializer)
        user = request.user
        self.check_object_permissions(request=request, obj=user)
        user = update_user(user=user, **request_serializer.validated_data)
        response_serializer = self.ResponseSerializer(user)
        return Response({
            'user': response_serializer.data
        }, status=status.HTTP_200_OK)


class UserChangePasswordApi(APIView):
    permission_classes = [UserPermission, ]

    class RequestSerializer(serializers.Serializer):
        old_password = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)
        password = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)
        password_confirm = serializers.CharField(required=True, max_length=settings.CHARFIELD_LENGTH)

    class ResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'name', 'email', 'tel']

    def put(self, request):
        request_serializer = self.RequestSerializer(data=request.data)
        validate_serializer(serializer=request_serializer)
        user = request.user
        self.check_object_permissions(request=request, obj=user)
        user = change_password(user=user, **request_serializer.validated_data)
        response_serializer = self.ResponseSerializer(user)
        return Response({
            'user': response_serializer.data
        }, status=status.HTTP_200_OK)


class UserListProjectsApi(APIView):
    class RequestSerializer(serializers.Serializer):
        project_id = serializers.IntegerField(required=True)

    class ResponseSerializer(serializers.ModelSerializer):
        model = Project

    def get(self, request, user_id):
        user = get_user_by(id=user_id)
        projects = get_projects_by(admin=user)
        response_serializer = self.ResponseSerializer(projects, many=True)
        return Response({
            'projects': response_serializer.data
        }, status=status.HTTP_200_OK)
