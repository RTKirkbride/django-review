from django.views.generic import ListView, DetailView

from .models import Restaurant, Review


class RestaurantListView(ListView):
    """Restaurant List View"""

    model = Restaurant
    template_name = "home.html"


class RestaurantReviewDetail(DetailView):
    """Review list view"""

    model = Review
    template_name = "restaurant_reviews.html"
