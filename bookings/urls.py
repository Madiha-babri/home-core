from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateBookingView.as_view(), name='booking'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('confirmation/', views.booking_confirmation, name='appointment_confirmation'),
    path('list/', views.booking_list, name='booking_list'),
    path('update/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('', views.bedrooms, name='bedrooms'),  # The empty string will map to the bedrooms view
    path('', views.kitchen, name='kitchen'),
    path('', views.washroom, name='washroom'),
    path('', views.livingrooms, name='livingrooms'),
]