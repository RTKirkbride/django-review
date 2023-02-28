from django.urls import path
from .views import RestaurantListView, RestaurantReviewDetail

urlpatterns = [
    path(
        "Restaurant/<int:pk>/",
        RestaurantReviewDetail.as_view(),
        name="restaurant_reviews",
    ),
    path("", RestaurantListView.as_view(), name="home"),
]
