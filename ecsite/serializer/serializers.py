from rest_framework import serializers
from ecsite.model.request_models import Userinfo, SampleData
from ecsite.model.pulldown_model import PulldownSelect


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ['name', 'sex', 'age', 'info', 'hobby']


class SampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = "__all__"

class PulldownSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PulldownSelect
        fields = "__all__"
