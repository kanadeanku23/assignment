from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ProjectViewSet, OrderViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('projects', ProjectViewSet, basename='projects')
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = router.urls
