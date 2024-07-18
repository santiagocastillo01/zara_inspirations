from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import add_perfume, add_perfume_woman, edit_profile, change_password
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home"),
   
    path('categoria_perfumes/', views.categoria_perfumes, name='categoria_perfumes'),
    path('categoria_inspiraciones/', views.categoria_inspiraciones, name='categoria_inspiraciones'),
    
    path('sobre_mi', views.sobre_mi, name='sobre_mi'),
   
    path('perfumes/', views.perfumes, name='perfumes'),
    path('perfumes/<int:perfume_id>/', views.perfume_detail, name='perfume_detail'),
    path('perfume/<int:perfume_id>/edit/', views.edit_perfume, name='edit_perfume'),
    path('perfume/<int:perfume_id>/delete/', views.delete_perfume, name='delete_perfume'),
    path('add_perfume/',add_perfume, name='add_perfume'),
    path('inspiraciones/', views.inspiraciones, name='inspiraciones'),
    
    

    path('perfumes_woman/', views.perfumes_woman, name='perfumes_woman'),
    path('inspiraciones_woman/', views.inspiraciones_woman, name='inspiraciones_woman'),
    path('perfume_woman/<int:perfume_id>/', views.perfume_woman_detail, name='perfume_woman_detail'),
    path('perfume_woman/<int:perfume_id>/edit/', views.edit_perfume_woman, name='edit_perfume_woman'),
    path('perfume_woman/<int:perfume_id>/delete/', views.delete_perfume_woman, name='delete_perfume_woman'),
    path('add_perfume_woman/', add_perfume_woman, name='add_perfume_woman'),
    
    
    
    
    path("login/", views.loginRequest, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("perfil/", views.perfil, name="perfil"),
    path('subir-avatar/', views.upload_avatar, name='upload_avatar'),
    path('eliminar-avatar/', views.delete_avatar, name='delete_avatar'),
    path('perfil/editar/', edit_profile, name='edit_profile'),
    path('perfil/cambiar_contraseña/', change_password, name='change_password'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

