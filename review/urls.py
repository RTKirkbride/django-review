from django.urls import path
from .views import review

urlpatterns = [
    path("", review.as_view(), name="home"),
]
