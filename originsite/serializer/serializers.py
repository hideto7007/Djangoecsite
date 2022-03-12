from rest_framework import serializers
from originsite.model.models import Userinfo, SampleData


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ['name', 'sex', 'age', 'info', 'hobby']


class SampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = "__all__"


