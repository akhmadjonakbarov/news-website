from django.urls import path
from api.views import sub_category_views

urlpatterns = [
    path('', sub_category_views.SubCategoryListView.as_view(), name='get_categories'),
    path('add-subcategory/', sub_category_views.SubCategoryAddView.as_view(),
         name='add_subcategory'),
    path('update-subcategory/<str:id>/', sub_category_views.SubCategoryEditView.as_view(),
         name='updated_subcategory'),
    path('delete-subcategory/<str:id>/', sub_category_views.SubCategoryDeleteView.as_view(),
         name='delete_subcategory')
]
