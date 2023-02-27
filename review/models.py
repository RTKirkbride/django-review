from django.db import models
from django.urls import reverse
from restaurant.models import Restaurant  # Trying something New


class Review(models.Model):
    """Review model class"""

    restaurants = models.ForeignKey(
        # "restaurant_name",
        Restaurant,  # Trying something New
        on_delete=models.CASCADE,
    )

    username = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    review_title = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField(max_length=500)
    rating = models.IntegerField(default=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.reviews

    def get_absolute_url(self):
        return reverse("reviews_detail", kwargs={"pk": self.pk})
