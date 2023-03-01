from django.urls import path
from .views import (
    RestaurantListView,
    RestaurantDetailView,
    ReviewCreateView,
    ReviewDetailView,
    ReviewEditView,
    ReviewDeleteView,
)

urlpatterns = [
    path("Review/new/", ReviewCreateView.as_view(), name="review_new"),
    path("Review/<int:pk>/", ReviewDetailView.as_view(), name="reveiw_detail"),
    path("Review/<int:pk>/edit/", ReviewEditView.as_view(), name="review_edit"),
    path("Review/<int:pk>/delete/", ReviewDeleteView.as_view(), name="reveiw_delete"),
    path(
        "Restaurant/<int:pk>/",
        RestaurantDetailView.as_view(),
        name="restaurant_detail",
    ),
    path("", RestaurantListView.as_view(), name="home"),
]
