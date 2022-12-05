from typing import List
from core.filters import BaseFilter, FilterParam


class SaleFilter(BaseFilter):
    query_params: List[FilterParam] = [
        FilterParam('invoice', {'type': 'string'}, 'invoice__icontains'),
        FilterParam('initial_date', {'type': 'string'}, 'date__gte'),
        FilterParam('end_date', {'type': 'string'}, 'date__lte'),
    ]
