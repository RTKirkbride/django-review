from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Restaurant, Review


class RestaurantListView(ListView):
    """Restaurant List View"""

    model = Restaurant
    template_name = "home.html"


class RestaurantDetailView(DetailView):
    """Review list view"""

    model = Restaurant
    template_name = "restaurant_detail.html"


class ReviewCreateView(CreateView):
    """Review Create View"""

    model = Review
    template_name = "review_new.html"
    fields = ["restaurant", "rating", "author", "body"]


class ReviewDetailView(DetailView):
    """ "Review Detail View"""

    model = Review
    template_name = "review_detail.html"


class ReviewEditView(UpdateView):
    """Review edit View"""

    model = Review
    template_name = "review_edit.html"


class ReviewDeleteView(DeleteView):
    """Review delete View"""

    model = Review
    template_name = "review_delete.html"
