from rest_framework import serializers
from app.models import Bug

"""
 Serializers Bug model 
"""
class BugSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bug
		fields = ('project','description','date_added')