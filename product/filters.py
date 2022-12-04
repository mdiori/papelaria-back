from typing import List
from core.filters import BaseFilter, FilterParam


class ProductFilter(BaseFilter):
    query_params: List[FilterParam] = [
        FilterParam('name', {'type': 'string'}, 'name__contains'),
        FilterParam('description', {'type': 'string'},
                    'description__contains'),
        FilterParam('active', {'type': 'boolean'}, 'active')
    ]
