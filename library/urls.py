from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from library import views

urlpatterns=[
    path('/autor',views.AutorView.as_view(), name='autor'),
    path('/autor/<int:pk>', views.AutorDetail.as_view(), name='autor_detail'),
    path('/libro', views.LibroView.as_view(), name='libro'),
    path('/libro/<int:pk>', views.LibroDetail.as_view(), name='libro_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)