from django.urls import path
from api.views import new_views

urlpatterns = [
    path('', new_views.NewListView.as_view(), name="get_news"),
    path('detail-new/<str:id>/', new_views.NewDetailView.as_view(), name='detail_view'),
    path('update-new/<str:id>/', new_views.NewDetailView.as_view(), name='detail_view'),
    path('delete-new/<str:id>/', new_views.NewDetailView.as_view(), name='detail_view'),
]