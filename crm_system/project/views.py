from .serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Project
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Project.objects.none
    
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.save()
 
    def get_queryset(self):
        if (self.request.user.is_superuser):
            return Project.objects.all()
        return Project.objects.filter(created_by=self.request.user)