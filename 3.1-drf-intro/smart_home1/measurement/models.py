from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete = models.CASCADE)
    temperature = models.FloatField(default=0)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.temperature} at {self.date_time}"