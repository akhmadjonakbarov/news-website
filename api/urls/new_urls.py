from django.urls import path
from api.views import new_views

urlpatterns = [
    path('', new_views.NewListView.as_view(), name="get_news"),
    path('get-mobile/', new_views.NewMobileListView.as_view(), name='get_mobile_news'),
    path('add/', new_views.NewAddView.as_view(), name='add_new'),
    path('detail/<str:id>/', new_views.NewDetailView.as_view(), name='detail_new'),
    path('update/<str:id>/', new_views.NewUpdateView.as_view(), name='update_new'),
    path('delete/<str:id>/', new_views.NewDeleteView.as_view(), name='delete_new'),
    path('add-comment/', new_views.CommentAddView.as_view(), name='add_comment')
]
