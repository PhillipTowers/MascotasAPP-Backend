from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, LugarViewSet, PostViewSet,
    ComentarioViewSet, FavoritoViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'lugares', LugarViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'favoritos', FavoritoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
