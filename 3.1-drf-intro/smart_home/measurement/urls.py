from django.urls import path
from .views import View, SensorView

urlpatterns = [
    path('view/', View.as_view()),
    path('sensor/<pk>/',SensorView.as_view())
]
