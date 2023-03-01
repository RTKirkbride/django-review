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
        return reverse("restaurant_detail", kwargs={"pk": self.pk})


class Review(models.Model):
    """Review model class"""

    restaurant = models.ForeignKey(
        # "restaurant_name",
        Restaurant,  # Trying something New
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    author = models.ForeignKey(  # changed to author
        "auth.user",
        on_delete=models.CASCADE,
        related_name="user",
    )

    review_title = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField(max_length=500)
    rating = models.IntegerField(default=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.review_title

    def get_absolute_url(self):
        return reverse("restaurant_detail", kwargs={"pk": self.pk})
