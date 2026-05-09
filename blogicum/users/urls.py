from django.urls import path
from .views import SignUpView

app_name = 'users'

urlpatterns = [
    path('registration/', SignUpView.as_view(), name='registration'),
]
