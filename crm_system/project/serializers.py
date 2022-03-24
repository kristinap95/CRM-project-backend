from re import S
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
        if not self.context['request'].user.is_superuser:
            instance.status = validated_data.get('status', instance.status)    
        return instance


    def create(self, validated_data):
        return Project.objects.create(
                title = validated_data['title'],
                description = validated_data['description'],
                deadline = validated_data['deadline'],
                status = validated_data['status'],
                created_by = validated_data['created_by'],
        )

