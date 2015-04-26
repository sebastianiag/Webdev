from rest_framework import serializers

from User.serializers import UserSerializer
from Post.models import Posts, Tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'tag')

class PostSerializer(serializers.ModelSerializer):
    author =  UserSerializer(read_only=True, required=False)
    tags = TagSerializer()
    class Meta:
        model = Posts
        fields = ('id', 'author', 'content', 'created_at', 'postTo', 'replyTo', 'tags')

        def get_validation_exclusions(self, *args, **kwargs):
            exclusions = super(PostSerializer, self).get_validation_exclusions()

            return exclusions + ['author']
