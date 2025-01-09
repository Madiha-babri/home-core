from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='gallery'),
     path('bedrooms/', views.bedrooms, name='bedrooms'),  # The empty string will map to the bedrooms view
    path('kitchen/', views.kitchen, name='kitchen'),
    path('washroom/', views.washroom, name='washroom'),
    path('livingrooms', views.livingrooms, name='livingrooms'),

]