from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404

from .models import Item


def item_list(request):
    """Return a JSON list of all items."""
    items = list(Item.objects.values('id', 'name', 'description', 'price', 'stock'))
    return JsonResponse({'items': items})


def item_detail(request, pk):
    """Return details for a single item."""
    item = get_object_or_404(Item, pk=pk)
    data = {
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': str(item.price),
        'stock': item.stock,
    }
    return JsonResponse({'item': data})

