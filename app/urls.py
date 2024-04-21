from django.urls import path
from .views import loginView, homeView

urlpatterns = [
    path('', loginView, name='login'),
    path('home/', homeView, name='home'),
]
