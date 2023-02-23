from django.urls import path
from .views import restaurant

urlpatterns = [
    path("", restaurant.as_view(), name="home"),
]
