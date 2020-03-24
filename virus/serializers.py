from rest_framework import serializers
from .models import Nhandan_Title, VnExpress, Moh_Number, Moh_Tracker


class NhandanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nhandan_Title
        fields = ('news_title', 'page_link' ,'summary', 'img',)


class VnExpressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VnExpress
        fields = ('news_title', 'page_link' ,'summary', 'img',)


class Moh_NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moh_Number
        fields = ('moh_number',)

class Moh_TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moh_Tracker
        fields = ('location','tracker',)