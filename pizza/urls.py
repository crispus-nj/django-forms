from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('order', views.order, name='order'),
    path('pizza',views.pizzas, name='pizzas'),
    path('order/<int:pk>',views.edit_order, name='edit_order'),
]
