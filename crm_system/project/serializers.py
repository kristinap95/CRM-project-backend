from urllib import request
from rest_framework import serializers
from .models import Project
from datetime import date

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'description', 'deadline', 'status', 'created_by')

    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError("You can't choose a date from the past.")
        return value
    
    def update(self, instance, validated_data):
        if self.context['request'].user.is_superuser:
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.deadline = validated_data.get('deadline', instance.deadline)
            instance.status = validated_data.get('status', instance.status)
            instance.created_by = validated_data.get('created_by', instance.created_by)
        else:
            instance.status = validated_data.get('status', instance.status)
            
        return instance
