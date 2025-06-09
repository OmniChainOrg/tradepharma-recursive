# ds_bot/views.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.db.models import Q

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        search_term = self.request.query_params.get('search', None)
        if search_term:
            queryset = queryset.filter(
                Q(name__icontains=search_term) |
                Q(description__icontains=search_term)
            )
        return queryset
