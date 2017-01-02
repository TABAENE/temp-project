from rest_framework import serializers
from models import BlogModel

# Serializers define the API representation.
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogModel
        fields = ('id', 'comment', 'posted_date', 'author')