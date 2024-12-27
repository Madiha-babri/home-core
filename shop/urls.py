from . import views
from django.urls import path

urlpatterns = [
    path('', views.shop_list, name='shop'),
]