# Write serializers here
from rest_framework import serializers

from models import Member, Book_master
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('first_name', 'email', 'is_deleted', 'expires_on')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_master
        fields = ('title', 'isbn', 'author', 'is_deleted')