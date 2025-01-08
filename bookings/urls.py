from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_appointment, name='bookings'),
    path('confirmation/', views.booking_confirmation, name='appointment_confirmation'),
    path('list/', views.booking_list, name='booking_list'),
    path('update/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('delete/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('', views.bedrooms, name='bedrooms'),  # The empty string will map to the bedrooms view
    path('kitchen/', views.kitchen, name='kitchen'),
    path('washroom/', views.washroom, name='washroom'),
    path('livingrooms', views.livingrooms, name='livingrooms'),

]