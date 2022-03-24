from .serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Project
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from datetime import date

# Create your views here
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Project.objects.none
    
    def perform_create(self, serializer):
        if not self.request.user.is_superuser:
            obj = serializer.save(created_by=self.request.user)
        else:
            obj = serializer.save() 
        obj.save()

    def partial_update(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            kwargs['partial'] = True
            
            return self.update(request, *args, **kwargs)
 
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Project.objects.all()
        return Project.objects.filter(created_by=self.request.user)