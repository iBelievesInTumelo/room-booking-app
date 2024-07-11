from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, BookingsView, RoomView,RegisterRoomView
from .views import UserBookings


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('bookings', BookingsView.as_view()),
    path('bookings/<pk>', BookingsView.as_view()),
    path('rooms', RoomView.as_view()),
    path('roomregister', RegisterRoomView.as_view()),
    path('userbookings', UserBookings.as_view()),
]