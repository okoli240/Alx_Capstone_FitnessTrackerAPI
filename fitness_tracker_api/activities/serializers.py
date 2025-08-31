from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    # Show the username instead of just user ID
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'date', 'notes']

    # Extra validation for clean data
    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be greater than 0 minutes.")
        return value

    def validate_distance(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Distance cannot be negative.")
        return value
