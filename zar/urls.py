from django.urls import path, include
from zar.views import*
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name="home"),
    path('inspiraciones/',views.inspiraciones, name='inspiraciones'),
    path('contacto',views.contacto, name='contacto'),
    path('perfumes/',views.perfumes, name='perfumes'),
    path('perfumes/<int:perfume_id>/', views.perfume_detail, name='perfume_detail'),
    path('perfume_woman/<int:perfume_id>/', perfume_woman_detail, name='perfume_woman_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)