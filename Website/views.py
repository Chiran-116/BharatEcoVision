from django.shortcuts import render,HttpResponse
from .models import Login


# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        login_id = request.POST['login_id']
        password = request.POST['password']
        try:
            login = Login.objects.get(login_id=login_id)
            if login.password == password:
                return render(request,"index.html")
            else:
                return HttpResponse("Invalid Password")
        except:
            return HttpResponse("Invalid Login ID")
    elif request.method == 'GET':
        return render(request,"login.html")
    else:
        return HttpResponse("Invalid request")

def land_inventory(request):
    return render(request,"land-inventory.html")

def applicant(request):
    return render(request,"applicant.html")

def app_payment(request):
    return render(request,"app_payment.html")

def app_profile(request):
    return render(request,"app_profile.html")

def drone(request):
    return render(request,"drone.html")

def contact_us(request):
    return render(request,"contact_us.html")

def app_status(request):
    return render(request,"app_status.html")

def implementing_home(request):
    return render(request,"implementing_home.html")

def nodal(request):
    return render(request,"nodal.html")

def app_apply(request):
    return render(request,"app_apply.html")

def imp_apply(request):
    return render(request,"imp_apply.html")

def imp_profile(request):
    return render(request,"imp_profile.html")



def imp_transaction(request):
    return render(request,"imp_transaction.html")

def nod_drone(request):
    return render(request,"nod_drone.html")

def nod_profile(request):
    return render(request,"nod_profile.html")

