from rest_framework import serializers
from tasks.models import Task

class Taskserialize(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"