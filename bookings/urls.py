from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateBookingView.as_view(), name='booking'),
    path('create/', views.create_booking, name='create_booking'),
    path('list/', views.booking_list, name='booking_list'),
    path('update/<int:booking_id>/', views.update_booking, name='update_booking'),
]