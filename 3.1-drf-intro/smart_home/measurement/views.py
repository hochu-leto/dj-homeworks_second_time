# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, \
    CreateAPIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorsSerializer


#  эта вьюха создаёт новое измерение
# отрабатываем пункты
# 3 # добавление измерения
# POST {{baseUrl}}/measurements/


class MeasuresView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


#  эта вьюха показывает список всех датчиков и позволяет создать новый
# отрабатываем пункты
# 1 # создание датчика
# POST {{baseUrl}}/sensors/
#
# 4 # получение датчиков
# GET {{baseUrl}}/sensors/


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

#  эта вьюха показывает конкретный датчик и позволяет его изменять
# отрабатываем пункты
# 5 # получение информации по датчику
# GET {{baseUrl}}/sensors/1/
# 2 # обновление датчика
# PATCH {{baseUrl}}/sensors/1/


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

