from django.urls import path

from .views import Login, Logout, CreateUserView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', CreateUserView.as_view(), name='register')
]