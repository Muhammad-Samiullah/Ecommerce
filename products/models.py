from django.db import models
from datetime import datetime


class Product(models.Model):
    productName = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    image_url = models.CharField(max_length=500)
    stock = models.IntegerField()

    def __str__(self):
        return f"Product Name: {self.productName} - Product Price: {self.price} - StocK: {self.stock}"


class Order(models.Model):
    customerFirstName = models.CharField(max_length=50)
    customerLastName = models.CharField(max_length=50)
    customerEmailAddress = models.CharField(max_length=150)
    customerAddress = models.CharField(max_length=500)
    customerCity = models.CharField(max_length=50)
    customerPostalCode = models.IntegerField()
    customerPhoneNumber = models.IntegerField()
    publishDate = models.DateTimeField(default=datetime.now())
    productID = models.ForeignKey(
        Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"CustomerName: {self.customerFirstName} {self.customerLastName} - {self.publishDate}"
