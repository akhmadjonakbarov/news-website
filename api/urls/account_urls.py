from django.urls import path
from api.views import account_views

urlpatterns = [
    path('', account_views.LoginView.as_view(), name='dashboard')
]