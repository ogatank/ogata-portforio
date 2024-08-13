from django.contrib import admin
from django.urls import path, include
from crud import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from ckeditor_uploader import views as uploader_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.top, name='top'),
    path('contact/', views.contact_view, name='contact'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditorのURLを追加
    url(r'^upload/', uploader_views.upload, name='ckeditor_upload'),
    url(r'^browse/', uploader_views.browse, name='ckeditor_browse'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
