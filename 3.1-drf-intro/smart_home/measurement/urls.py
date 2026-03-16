from django.urls import path

from .views import SensorListCreateView, SensorDetailUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<int:pk>/', SensorDetailUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
