from django.urls import path, include
from .views import ProjectViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = router.urls
