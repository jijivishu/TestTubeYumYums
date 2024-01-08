# Django REST based import
from rest_framework import serializers

# Internal import
from .models import Range, CBC, VitMin, CBCStat, VitMinStat

# TODO: Describe the purpose of each serializer in comments

# Basic model serializer for CBC model
class CBCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBC
        fields = '__all__'


# Basic model serializer for VitMin model
class VitMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitMin
        fields = '__all__'


# Basic model serializer for Range model
class RangeSerializer(serializers.ModelSerializer):
    cbc_upper = CBCSerializer()
    cbc_lower = CBCSerializer()
    vitmin_upper = VitMinSerializer()
    vitmin_lower = VitMinSerializer()
    class Meta:
        model = Range
        fields = ['cbc_upper', 'cbc_lower', 'vitmin_upper', 'vitmin_lower']


# Basic model serializer for CBCStat model
class CBCStatSerializer(serializers.ModelSerializer):
    cbc = CBCSerializer()
    upper_range = CBCSerializer()
    lower_range = CBCSerializer()
    class Meta:
        model = CBCStat
        fields = ['cbc', 'upper_range', 'lower_range']


# Basic model serializer for VitMinStat model
class VitMinStatSerializer(serializers.ModelSerializer):
    vitmin = VitMinSerializer()
    upper_range = VitMinSerializer()
    lower_range = VitMinSerializer()
    class Meta:
        model = VitMinStat
        fields = ['vitmin', 'upper_range', 'lower_range']
