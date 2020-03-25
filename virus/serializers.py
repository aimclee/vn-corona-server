from rest_framework import serializers
from .models import Nhandan_Title, VnExpress, Moh_Tracker, WorldMeter


class NhandanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nhandan_Title
        fields = ('news_title', 'page_link' ,'summary', 'img',)


class VnExpressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VnExpress
        fields = ('news_title', 'page_link' ,'summary', 'img',)



class Moh_TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moh_Tracker
        fields = ('location','tracker',)


class WorldMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldMeter
        fields = ('total_infected','total_death', 'total_recovery','new_infected',)