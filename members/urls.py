from django.urls import path

from members.views import UserRegistrationView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
]
