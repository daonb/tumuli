from rest_framework import serializers
from biography.models import Memoir, Period, Biography, ContentAtom
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class MemoirSerializer(serializers.ModelSerializer):

    class Meta:
        model = Memoir
        fields = ('owner', 'author', 'period', 'content', 'story_audio',
                  'story_text', 'notes', 'created', 'modified')


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = ('name', 'story_audio', 'notes', 'place',
                  'start_date', 'end_date', 'biography')


class BiographySerializer(serializers.ModelSerializer):

    class Meta:
        model = Biography
        fields = ('uuid', 'date_of_birth', 'date_of_passing',
                  'place_of_birth', 'place_of_passing', 'user',
                  'editors', 'creator', 'is_public', 'created', 'modified')


class ContentAtomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentAtom
        fields = ('owner', 'placed', 'periods',
                  'who', 'where', 'date', 'image')
