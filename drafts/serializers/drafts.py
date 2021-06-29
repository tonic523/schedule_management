from rest_framework import serializers

from drafts.models.drafts import Draft
from permissions.serializers.roles import Role, RoleSerializer

class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        #exclude = ['drafter']
        fields = '__all__'