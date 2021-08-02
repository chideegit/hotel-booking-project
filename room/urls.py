from django.urls import path
from .views import Dashboard, BookRoomView, AllGuestsView, CheckOutView, GuestHistoryView

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('book-room/', BookRoomView, name='book-room'),
    path('all-guests/', AllGuestsView, name='all-guests'),
    path('check-out/<int:pk>/', CheckOutView, name='check-out'),
    path('guest-history/', GuestHistoryView, name='guest-history')
]
