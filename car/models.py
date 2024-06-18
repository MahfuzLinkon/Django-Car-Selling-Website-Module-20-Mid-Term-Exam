from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.FloatField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/car/")

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment by {self.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
