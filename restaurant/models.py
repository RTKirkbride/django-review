from django.db import models
from django.urls import reverse


class Restaurant(models.Model):
    """Restaurant model class"""

    restaurant_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.restaurant_name

    def get_absolute_url(self):
        """Get absolute URL"""
        return reverse("reviews_detail", kwargs={"pk": self.pk})
