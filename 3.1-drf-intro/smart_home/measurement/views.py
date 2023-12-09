# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementDetailSerializer, MeasurementSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.views import APIView



'''@api_view(['GET'])
def view(request):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many = True)
        return(Response(ser.data))
    if request.method == 'POST':
        pass
    '''


class View(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementDetailSerializer
    
