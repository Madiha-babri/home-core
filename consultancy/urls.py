from django.urls import path
from . import views


urlpatterns = [
    path('book_consultancy/', views.book_consultancy, name='consultancy'),
]