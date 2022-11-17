from django.urls import path
from .views import item, buy_item, index

urlpatterns = [
    path('', index, name='index'),
    path('item/<int:id>/', item, name='item'),
    path('buy/<int:id>/', buy_item, name='buy'),
]
