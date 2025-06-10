# ds_bot/views.py

from rest_framework import viewsets, generics, permissions
from rest_framework.filters import SearchFilter
from django.db.models import Q

from ds_bot.models import Item, Match
from ds_bot.serializers import ItemSerializer, MatchSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint pour gérer les items.
    Possibilité de recherche par nom ou description via ?search=...
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    permission_classes = [permissions.AllowAny]  # À adapter selon vos besoins

    def get_queryset(self):
        """
        Filtre les items en fonction d'un terme de recherche.
        """
        queryset = Item.objects.all()
        search_term = self.request.query_params.get('search', None)

        if search_term:
            queryset = queryset.filter(
                Q(name__icontains=search_term) |
                Q(description__icontains=search_term)
            )

        return queryset


class MatchList(generics.ListAPIView):
    """
    API endpoint pour récupérer tous les matches.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.AllowAny]  # À modifier si nécessaire
