from rest_framework import serializers
from .models import Nhandan_Title


class NhandanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nhandan_Title
        fields = ('news_title', 'summary', 'img',)