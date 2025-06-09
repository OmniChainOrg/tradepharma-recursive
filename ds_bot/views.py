# ds_bot/views.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.db.models import Q
from rest_framework import generics
from ds_bot.models import Item
from ds_bot.serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
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

class MatchList(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
