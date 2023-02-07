from django.urls import path
from api.views import category_views



urlpatterns = [
    path('', category_views.CategoryListView.as_view(), name='get_categories'),
    path('add/', category_views.CategoryAddView.as_view(),
         name='add_category'),
    path('update/<str:id>/', category_views.CategoryEditView.as_view(),
         name='updated_category'),
    path('delete/<str:id>/', category_views.CategoryDeleteView.as_view(),
         name='delete_category')
]
