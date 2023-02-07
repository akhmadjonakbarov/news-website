from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/', include('api.url')),
    path('api/categories/', include('api.urls.category_urls')),
    path('api/sub-categories/', include('api.urls.sub_category_urls')),
    path('api/news/', include('api.urls.new_urls')),
    path('api/slider/', include('api.urls.slider_urls')),
    path('api/contact/', include('api.urls.contact_urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
