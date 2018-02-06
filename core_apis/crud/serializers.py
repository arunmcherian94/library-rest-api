# Write serializers here
from rest_framework import serializers

from models import Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('first_name', 'email', 'is_deleted', 'expires_on')