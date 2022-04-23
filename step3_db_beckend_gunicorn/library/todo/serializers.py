from rest_framework import serializers
from .models import ProjectModel, TodoModel


class ProjectModelSerializers(serializers.ModelSerializer):
    set_todo = serializers.SerializerMethodField()
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = ProjectModel
        fields = '__all__'

    def get_set_todo(self, obj):
        a = []
        for i in TodoModel.objects.filter(project=obj.pk):
            a.append(str(i))
        return a


class ProjectModelSerializersPost(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class TodoModelSerializers(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    users = serializers.StringRelatedField()

    class Meta:
        model = TodoModel
        fields = '__all__'


class TodoModelSerializersPost(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'
