from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.



def item_list(request):
    # """
    # View to display all ACTIVE items.
    # """

    items = Item.objects.filter(is_active=True)

    context = {
        'items': items
    }
    return render(request, 'market/item_list.html', context)


def item_detail(request, pk):
    # """
    # View to display single item detail.
    # """
    item = get_object_or_404(Item, pk=pk, is_active=True)

    context = {
        'item': item
    }
    return render(request, 'market/item_detail.html', context)