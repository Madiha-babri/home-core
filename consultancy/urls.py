from django.urls import path
from . import views
from .views import EditBooking, DeleteBooking


urlpatterns = [
    path('book_consultancy/', views.book_consultancy, name='consultancy'),
    path("booking_edit/<int:pk>/", views.EditBooking.as_view(), name='edit_booking'),
    path('delete_booking/<int:pk>', views.DeleteBooking.as_view(), name='delete_booking'),
]

