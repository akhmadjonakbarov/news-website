from django.urls import path
from api import view

urlpatterns = [
    path('', view.RoutesView.as_view()),
]
