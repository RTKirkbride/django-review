from django.contrib.auth.forms import UserCreationForm

"""Name: Ryan Kirkbtride
   Date: 3/1/23
   Class: CIS218 Barnes
"""
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    """Sign up View"""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
