from django.views.generic import ListView

from .models import Restaurant


class restaurant(ListView):
    """Restaurant List View"""

    model = Restaurant
    template_name = "home.html"
