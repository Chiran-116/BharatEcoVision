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