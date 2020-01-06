from rest_framework import serializers
from taskmanagement.models import Task


class TaskSerializer(serializers.ModelSerializer):
    # create a Serializer class with fields that correspond to the Model fields
    # allow complex data such as querysets and model instances to be converted to
    # native Python datatypes that can then be easily rendered into JSON, XML.
    class Meta:
        model = Task
        fields = ('title', 'description', 'assigned_to', 'created_by')
        extra_kwargs = {'description': {'allow_null': True}}

        # custom field level validation
        # def validate_title(self, value):
