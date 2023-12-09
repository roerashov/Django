from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        #fields = ['id','name','description']
        fields = '__all__'

class MeasurementSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
        #fields = ['temperature','date_time']



class MeasurementDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id','name','description', 'measurement']
