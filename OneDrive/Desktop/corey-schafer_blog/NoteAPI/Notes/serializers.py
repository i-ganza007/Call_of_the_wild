from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = (
            'idx',
            'name',
            'description',
            'created_at',
            'last_updated',
            'status',
            'author'
        )

    def validate_name(self,value):
        if len(value) < 5:
            raise serializers.ValidationError('Name must be at least 3 characters long')
        return value