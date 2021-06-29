from rest_framework import serializers

from drafts.models.drafts import Draft

class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        fields = '__all__'