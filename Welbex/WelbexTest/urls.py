from django.urls import path
from .views import WelView



urlpatterns = [
    path('', WelView.as_view())
]