from django.urls import path
from api.views import contact_views

urlpatterns = [
    path('', contact_views.ContactView.as_view(), name='contact'),
]
