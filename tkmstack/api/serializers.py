from rest_framework import serializers
from .models import Stack,Tags,Answers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields=("tag_name",)



class StackSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True,queryset=Tags.objects.all(),slug_field='tag_name')
    answers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=Stack
        fields=("title","description","user","created_time","tags","answers")




class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ( 'user', 'stack', 'body', 'created')