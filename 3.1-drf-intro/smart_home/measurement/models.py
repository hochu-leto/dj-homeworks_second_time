from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    """Объект на котором проводят измерения."""
    name = models.TextField()
    description = models.TextField()


class Measurement(models.Model):
    """Измерение температуры на объекте."""
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    measure_time = models.DateTimeField(
        auto_now=True
    )
