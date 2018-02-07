# Write serializers here
from rest_framework import serializers

#Model imports
from models import Member, Book_master, BookAction

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('first_name', 'email', 'is_deleted', 'expires_on')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_master
        fields = ('title', 'isbn', 'author', 'is_deleted')

class BookActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_master
        fields = ('member', 'copy', 'borrowed_date', 'is_returned', 'due_date')