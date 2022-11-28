from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound


def get_or_404(klass, exception_message: str, *args, **kwargs):
    try:
        return get_object_or_404(klass, *args, **kwargs)
    except Http404 as e:
        raise NotFound(exception_message)
