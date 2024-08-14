from rest_framework import serializers
from .models import Department, Project, Writer, HireWriter


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.title
class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'

    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
class HireWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireWriter
        fields = '__all__'

    def __str__(self):
        """
        Return a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
