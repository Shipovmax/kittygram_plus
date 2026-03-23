from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet , LightCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')
router.register('owners', OwnerViewSet, basename='owners')
router.register(r'mycats', LightCatViewSet, basename='mycats')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
