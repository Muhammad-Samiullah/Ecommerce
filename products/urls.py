from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:product_id>', views.buy, name='buy'),
    path('order/<int:product_id>', views.orderReceived, name='order')
]
