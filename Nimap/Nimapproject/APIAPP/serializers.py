from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name', 'created_by', 'users', 'created_at']
    def get_client_name(self, obj):
        return obj.client.client_name
    def get_users(self, obj):

        return obj.created_by.created_by
    def get_created_by(self, obj):

        return obj.created_by.users
    def get_client(self, obj):
       return obj.client.client if obj.client else None    
