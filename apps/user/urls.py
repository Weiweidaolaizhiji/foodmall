from django.urls import path
from .views import LoginView,RegisterView,LogoutView

urlpatterns=[
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(), name='register'),

]