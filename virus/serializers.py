from rest_framework import serializers
from .models import Nhandan_Title, VnExpress


class NhandanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nhandan_Title
        fields = ('news_title', 'page_link' ,'summary', 'img',)


class VnExpressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VnExpress
        fields = ('news_title', 'page_link' ,'summary', 'img',)