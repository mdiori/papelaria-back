from typing import List
from core.filters import BaseFilter, FilterParam


class CommissionFilter(BaseFilter):
    query_params: List[FilterParam] = [
        FilterParam('week_day', {'type': 'integer'}, 'week_day__icontains'),
        FilterParam('active', {'type': 'boolean'}, 'active')
    ]
