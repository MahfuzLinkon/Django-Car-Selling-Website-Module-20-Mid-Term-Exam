from django.urls import path, include

from . import views

urlpatterns = [
    path("details/<int:id>/", views.CarDetails.as_view(), name="car_details"),
    path("order-car/<int:id>/", views.orderCar, name="order_car"),
]
