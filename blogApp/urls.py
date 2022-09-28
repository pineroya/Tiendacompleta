from django.urls import path
from blogApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog, name='Blog'),
    path('categoria/<categoria_id>/', views.categoria, name='Categoria'),
    path('formulario/', views.form_blog, name = 'Formulario_blog'),
    path('editar_blog/<titulo_blog>/', views.editar_blog, name = "Editar_blog"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)