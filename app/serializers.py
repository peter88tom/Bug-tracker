from rest_framework import serializers
from app.models import Bug, Project


"""
 Serialize Project Model
"""
class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'



"""
Serialize Bug Model
"""
class ProjectBugSerializer(serializers.ModelSerializer):
	project = ProjectSerializer()
	class Meta:
		model = Bug
		fields = '__all__'