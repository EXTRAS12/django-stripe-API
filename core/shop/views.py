import json
from shop.services.stripe import create_stripe_session
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render,  get_object_or_404
from .models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'shop/index.html', context={
        'items': items,
    })


def item(request, id):
    item =  get_object_or_404(Item, pk=id)
    return render(request, 'shop/detailitem.html', context={
        'item': item,
        'stripe_api': settings.STRIPE_PUB_KEY
    })


def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)

    stripe_session = create_stripe_session(
        secret_key=settings.STRIPE_SECRET_KEY,
        product_name=str(item),
        price=item.price*100,
        quantity=1,
        currency="usd",
        redirect_url=f'{settings.WEBSITE_URL}'
    )
    return JsonResponse(
        {
            "success": {
                "item": {"id": id},
                "stripe_session": {"id": stripe_session.stripe_id},
            },
        }
    )
