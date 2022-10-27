from rest_framework import serializers
from .models import BlogList


class BlogSerializer(serializers.ModelSerializer):
    """
    The Blog Serializer automatically create a serializer class
    with fields that correspond to the model field.

    """
    class Meta:
        model = BlogList
        fields = ('id',
                  'title',
                  'description',
                  'date_created',
                  'author_name',
                  'updated_on',
                  'status'
                  )
        read_only_fields=('date_created',)
