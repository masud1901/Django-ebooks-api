from rest_framework import pagination


class SmallSetPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10
    page_query_param = "page"
    max_page_size_query_param = "max_page_size"
