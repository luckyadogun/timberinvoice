from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    ordering = '-date_created'