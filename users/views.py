from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import RiderForm, CustomerrForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def riderReg(request):
    form = RiderForm()
        
    context = {
        "form":form
    }
    return render(request, "users/riderreg.html", context)


@login_required
def customerReg(request):
    try:
        user = request.user.customer
        form = CustomerrForm(instance=user)
        if request.method == "POST":
            form = CustomerrForm(request.POST, instance=user)
            print(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.customer = request.user
                form.save()
                
                return redirect("profile")
    except:
        form = CustomerrForm()
        if request.method =="POST":
            form = CustomerrForm(request.POST)
            if form.is_valid():
               form = form.save(commit=False)
               form.customer = request.user
               form.save()
               return redirect("profile")
                
    context = {
        "form":form
    }
    return render(request, "users/customer.html", context)

@login_required
def profile(request):
    return render(request, "users/profile.html")

def logOut(request):
    return render(request, "users/logout.html")