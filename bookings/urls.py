from django.urls import path
from . import views
from .views import EditBooking, DeleteBooking

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path("booking_edit/<int:pk>/", EditBooking.as_view(), name="edit_booking"),
    path("delete_booking/<int:pk>", DeleteBooking.as_view(),
        name="delete_booking"),
    path('', views.bedrooms, name='bedrooms'),  # The empty string will map to the bedrooms view
    path('kitchen/', views.kitchen, name='kitchen'),
    path('washroom/', views.washroom, name='washroom'),
    path('livingrooms', views.livingrooms, name='livingrooms'),

]