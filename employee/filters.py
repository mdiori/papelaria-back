from typing import List
from core.filters import BaseFilter, FilterParam


class EmployeeFilter(BaseFilter):
    query_params: List[FilterParam] = [
        FilterParam('name', {'type': 'string'}, 'name__icontains'),
        FilterParam('active', {'type': 'boolean'}, 'active')
    ]
