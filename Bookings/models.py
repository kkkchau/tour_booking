from django.db import models
from datetime import datetime


# Create your models here.

#Enum Class to populate the Booking Status of a tour
class Status(models.Model):
    STATUS = (
        ('МЕСТ НЕТ', "МЕСТ НЕТ"),
        ('ДОСТУПНО', "ДОСТУПНО"),
    )
    status = models.CharField(max_length=10, choices=STATUS, unique=True)

    def __str__(self):
        return self.status


class Tour(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    visitorCount = models.IntegerField(blank=True, null=True, default=0)
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"


class Customer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    address = models.TextField(blank=True ,null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Booking(models.Model):
    h_id = models.ForeignKey("Tour", on_delete=models.CASCADE)
    c_id = models.ForeignKey("Customer", on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)
    amount = models.FloatField(blank=True, null=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    checkInDate = models.DateField(auto_now_add=True,blank=True , null=True)
    checkOutDate = models.DateField(auto_now_add=True,blank=True ,null=True)

    def __str__(self):
        return str(self.h_id)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"



class Search(models.Model):
    c_id = models.ForeignKey("Customer", on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    checkInDate = models.DateField(blank=True,null=True)
    checkOutDate = models.DateField(blank=True , null=True)
    amount = models.FloatField(blank=True , null=True)

    def __str__(self):
        return str(self.c_id)