from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from omdb_app.views import FilmeViewSet, DiretorViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'filmes', FilmeViewSet)
router.register(r'diretores', DiretorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html'), name='home')
]
