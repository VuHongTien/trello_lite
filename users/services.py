from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from auth_tokens.services import expire_token
from utils.token_maker import generate_token
from utils.exceptions import *
from .models import User


def get_user_by(raise_exception=True, with_deleted=False, **kwargs):
    user = User.objects.all_with_deleted().filter(**kwargs).first() if with_deleted else User.objects.all().filter(
        **kwargs).first()
    if not user and raise_exception:
        raise ObjectNotFound
    return user


def create_user(**kwargs):
    password = kwargs.pop('password')
    password_confirm = kwargs.pop('password_confirm')
    email = kwargs.get('email')
    user = get_user_by(email=email, raise_exception=False, with_deleted=True)
    if user:
        raise DuplicateEntry(key='email', entry=email)
    if password != password_confirm:
        raise ValidationError(message='password and password_confirm must be the same')
    user = User.objects.create(**kwargs)
    user.set_password(password)
    user.save()
    return user


def authenticate_user(email, password):
    user = get_user_by(email=email)
    if not user.check_password(password):
        raise Unauthenticated(message='Incorrect email or password')
    return user


def change_password(user, **kwargs):
    old_password = kwargs.pop('old_password')
    authenticate_user(email=user.email, password=old_password)
    password = kwargs.pop('password')
    password_confirm = kwargs.pop('password_confirm')
    if password != password_confirm:
        raise ValidationError('password and password_confirm must be the same')
    user.set_password(raw_password=password)
    user.save()
    return user


def update_user(user, **kwargs):
    for (key, value) in kwargs.items():
        setattr(user, key, value)
    user.save()
    return user
