from django.urls import path
from api.views import slider_views

urlpatterns = [
    path('', slider_views.SliderListView.as_view(), name="get_sliders"),
    path('add/', slider_views.SliderAddView.as_view(), name='add_slider'),
    path('detail/<str:id>/', slider_views.SliderDetailView.as_view(), name='detail_slider'),
    path('update/<str:id>/', slider_views.SliderEditView.as_view(), name='update_slider'),
    path('delete/<str:id>/', slider_views.SliderDeleteView.as_view(), name='delete_slider'),
]