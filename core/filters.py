from typing import Any, Dict, List
from django.db.models import QuerySet
from rest_framework.views import APIView
from rest_framework.request import Request


class FilterParam:
    '''Describes a filter param.'''

    def __init__(self,
                 name: str,
                 openapi_schema: Dict[str, Any],
                 query_filter: str) -> None:
        '''Describe a FilterParam.

        Args:
            name: The name of the param.
            openapi_schema: The schema for the openapi specification.
            query_filter: The filter for Django ORM queryset.'''
        self.name = name
        self.openapi_schema = openapi_schema
        self.query_filter = query_filter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def openapi_schema(self) -> Dict[str, Any]:
        return self._openapi_schema

    @openapi_schema.setter
    def openapi_schema(self, openapi_schema: Dict[str, Any]):
        self._openapi_schema = openapi_schema

    @property
    def query_filter(self) -> str:
        return self._query_filter

    @query_filter.setter
    def query_filter(self, query_filter: str):
        self._query_filter = query_filter


class BaseFilter:
    query_params: List[FilterParam] = []

    def filter_queryset(self,
                        request: Request,
                        queryset: QuerySet,
                        view: APIView):
        filter_kwargs = {}
        apply_filter = False
        for param in self.query_params:
            value = request.query_params.get(param.name)
            if value:
                apply_filter = True
                filter_kwargs[param.query_filter] = value

        if apply_filter:
            return queryset.filter(**filter_kwargs)

        return queryset

    def get_schema_operation_parameters(self, view):
        return [
            {
                'name': param.name,
                'required': False,
                'in': 'query',
                'schema': param.openapi_schema
            } for param in self.query_params
        ]
