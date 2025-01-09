from django.urls import path
from . import views
from .views import EditBooking, DeleteBooking

urlpatterns = [
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path("booking_edit/<int:pk>/", EditBooking.as_view(), name="edit_booking"),
    path("delete_booking/<int:pk>", DeleteBooking.as_view(),
        name="delete_booking"),
]