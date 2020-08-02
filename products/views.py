from django.shortcuts import render
from .models import Product, Order
from datetime import datetime


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)


def buy(request, product_id):
    product = Product.objects.get(id=product_id)
    total_price = product.price + 50
    return render(request, 'products/form.html', {'product': product, 'total_price': total_price})


def orderReceived(request, product_id):
    firstName = request.POST.get('fname')
    lastName = request.POST.get('lname')
    email = request.POST.get('email')
    address = request.POST.get('address')
    city = request.POST.get('city')
    postalCode = request.POST.get('pcode')
    mobileNumber = request.POST.get('mnumber')
    product = Product.objects.get(id=product_id)
    product.stock -= 1
    currentTime = datetime.now()
    totalPrice = product.price + 50
    Order.objects.create(customerFirstName=firstName, customerLastName=lastName, customerEmailAddress=email,
                         customerAddress=address, customerCity=city, customerPostalCode=postalCode,
                         customerPhoneNumber=mobileNumber, productID=product)
    context = {
        'fname': firstName,
        'lname': lastName,
        'email': email,
        'address': address,
        'city': city,
        'postalCode': postalCode,
        'mobileNumber': mobileNumber,
        'product': product,
        'totalPrice': totalPrice
    }
    return render(request, 'products/order.html', context)
