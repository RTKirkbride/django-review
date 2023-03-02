"""Name: Ryan Kirkbtride
   Date: 3/1/23
   Class: CIS218 Barnes

"""


from django.urls import path

from .views import SignUpView

urlpatterns = [path("signup/", SignUpView.as_view(), name="signup")]
