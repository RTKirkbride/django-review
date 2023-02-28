from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Restaurant, Review


class RestaurantTests(TestCase):
    """Restaurant tests"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.restaurant = Restaurant.objects.create(
            restaurant_name="A good name",
            # created date field test content
            # updated date field test content
        )

        cls.review = Review.objects.create(
            review_title="A good title",
            body="Nice body content",
            email="email@email.com"
            # author = cls.user, # no author...
            # rating field test content
            # created date field test content
            # updated date field test content
        )

    def test_restaurant_model(self):
        """Test Restaurant model"""

        self.assertEqual(self.restaurant.restaurant_name, "A good name")
        self.assertEqual(str(self.restaurant), "A good title")
        self.assertEqual(self.restaurant.get_absolute_url(), "/restaurant/1/")

    def test_url_exists_at_correct_location_listview(self):
        """Test url exists at correct location listview"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        """Test url exists at correct location detail view"""
        response = self.client.get("/restaurant/1/")
        self.assertEqual(response.status_code, 200)

    def test_restaurant_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_restaurant_review_detailview(self):
        """Test restaurant detail view"""
        response = self.client.get(
            reverse("restaurant_review", kwargs={"pk": self.post.pk})
        )
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.asserContains(response, "A good title")
        self.assertTemplateUsed(response, "restaurant_reviews.html")

    def test_review_model(self):
        """Test Review model"""
        self.assertEqual(self.review.review_title, "A good title")
        self.assertEqual(self.review.body, "Nice body content")
        # self.assertEqual(self.review.author.username, "testuser") do I have a username field here?
        # self.assertEqual(self.review.email, "email@email.com") should this be with the user data?
        self.assertEqual(str(self.review), "A good title")
        self.assertEqual(self.review.get_absolute_url(), "/review/1/")
        # add test for rating
        # add test for create date
        # add test for update date
