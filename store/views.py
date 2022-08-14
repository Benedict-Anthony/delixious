from django.shortcuts import render
from .models import Product, OrderDetail, OrderItems, ShippingInfo
from users.models import Customer
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import json 
from django.core.paginator import Paginator
from decouple import config
from django.utils.text import slugify 
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "store/index.html")




def menu(request):
    products = Product.objects.all().order_by("-date_modified")
    paginator = Paginator(products, 9)
    page_num = request.GET.get("page")
    page_products =  paginator.get_page(page_num)
    context = {
        "products":page_products
    }
    return render(request, "store/menu.html", context)



@login_required
def checkout(request):
    return render(request, "store/checkout.html")



def shippingFunc(orderDetails, customer, customerData):
    shippingInfo, created = ShippingInfo.objects.get_or_create(orderDetails=orderDetails, customer=customer, state=customerData.get("state"), city=customerData.get("city"), town=customerData.get("town"), street=customerData.get("street"), description=customerData.get("description"))
    shippingInfo.save()
    return shippingInfo



def update_cart(request): 
    data = json.loads(request.body)
    storedItems = data.get("storedItems")
    if request.user.is_authenticated:

        customerData = data.get("customerInfo")
        customer = request.user.customer
        orderDetails, created= OrderDetail.objects.get_or_create(customer=customer, completed=False)
        
        shippingInfo=shippingFunc(orderDetails=orderDetails, customer=customer, customerData=customerData)
        for item in storedItems:
           product = Product.objects.get(id=item["id"])
           orderDetails, created = OrderDetail.objects.get_or_create(customer=customer, completed=False)
           orderItems = OrderItems.objects.create(orderDetails=orderDetails, product=product, quantity=item["quantity"])
           
           orderItems.total_amout = product.price * orderItems.quantity
           orderItems.shippingInfo = shippingInfo
           
           orderItems.save()
        return JsonResponse(customer.id, safe=False)
           
           
    else:
        customerData = data.get("customerInfo")
        customer, created = Customer.objects.get_or_create(first_name=customerData.get("firstName"),  last_name=customerData.get("lastName"), email=customerData.get("email"), contact=customerData.get("contact"))
        customer.save()
        
        orderDetails, created = OrderDetail.objects.get_or_create(customer=customer, completed=False)
        
        shippingInfo=shippingFunc(orderDetails=orderDetails, customer=customer, customerData=customerData)
        for item in storedItems:
           product = Product.objects.get(id=item["id"])
           orderDetails, created = OrderDetail.objects.get_or_create(customer=customer, completed=False)
           orderItems = OrderItems.objects.create(orderDetails=orderDetails, product=product, quantity=item["quantity"])
           
           orderItems.total_amout = product.price * orderItems.quantity
           orderItems.shippingInfo = shippingInfo
           
           orderItems.save()
        print(customer)
        return JsonResponse(customer.id, safe=False)
           
    # customerID = customer.id
    return JsonResponse("cart Items", safe=False)



def check_out_session(request, id):
    SECRET_KEY = config("SECRET_KEY")
    PUBLIC_KEY = config("PUBLISH_KEY")
    customer = Customer.objects.get(pk=id)
    orderDetails = OrderDetail.objects.get(customer=customer, completed=False)
    orderedItems = orderDetails.orderitems_set.all()
    sum = 0
    for item in orderedItems:
        sum+=item.total_amout
    
    def userStatus():
        if request.user.is_authenticated:
            return request.user.email
        else:
            return customer.email
        
    email=userStatus()
    
    context ={
        "sum":sum,
        "customer":customer,
        "orderedItems":orderedItems,
        "secretKey":SECRET_KEY,
        "publicKey":PUBLIC_KEY,
        "email":email
    }
    return render(request, "store/payment.html", context)

def sucess(request):
    orderDetails = OrderDetail.objects.filter(completed=False, status="pending")
    for item in orderDetails:
        item.completed=True
        item.status="sent"
        item.transanction_id = slugify(f'{item.date} {item.id} {item.customer.id}')
        
        item.save()
        
    return render(request, "store/success.html")
