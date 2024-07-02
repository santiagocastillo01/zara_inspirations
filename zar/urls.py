from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('categoria_inspiraciones/', views.categoria_inspiraciones, name='categoria_inspiraciones'),
    path('categoria_perfumes/', views.categoria_perfumes, name='categoria_perfumes'),
    path('inspiraciones/', views.inspiraciones, name='inspiraciones'),
    path('contacto', views.contacto, name='contacto'),
    path('perfumes/', views.perfumes, name='perfumes'),
    path('perfumes/<int:perfume_id>/', views.perfume_detail, name='perfume_detail'),
    path('perfumes_woman/', views.perfumes_woman, name='perfumes_woman'),
    path('inspiraciones_woman/', views.inspiraciones_woman, name='inspiraciones_woman'),
    path('perfume_woman/<int:perfume_id>/', views.perfume_woman_detail, name='perfume_woman_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" from django.urls import path, include
from zar.views import*
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name="home"),
    path('categoria_inspiraciones/',categoria_inspiraciones, name='categoria_inspiraciones'),
    path('categoria_perfumes/',categoria_perfumes, name='categoria_perfumes'),
    path('inspiraciones/',views.inspiraciones, name='inspiraciones'),
    path('contacto',views.contacto, name='contacto'),
    path('perfumes/',views.perfumes, name='perfumes'),
    path('perfumes/<int:perfume_id>/', views.perfume_detail, name='perfume_detail'),
    path('perfumes_woman/',views.perfumes_woman, name='perfumes_woman'),
    path('inspiraciones_woman/',views.inspiraciones_woman, name='inspiraciones_woman'),
    path('perfume_woman/<int:perfume_id>/', perfume_woman_detail, name='perfume_woman_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """