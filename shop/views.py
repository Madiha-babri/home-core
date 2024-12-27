from django.shortcuts import render
from .models import Shop


def shop_list(request):
    """
    Renders the Shop page
    """
    shop = Shop.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "shop/shop.html",
        {"shop": shop},
    )