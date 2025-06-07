# ds_bot/api.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(is_deleted=False)
    serializer_class = ItemSerializer
