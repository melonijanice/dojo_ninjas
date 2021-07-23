from .models import Dojo, Ninja
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    context={'all_dojos':Dojo.objects.all()}
    return render(request,'user_dash.html',context)


def create(request):
    if request.method == "POST":
        if 'add_user' in request.POST:
            Dojo.objects.create(name=request.POST["dojo_name"],city= request.POST["city"],state= request.POST["state"],desc=request.POST["desc"])
        if 'add_ninja' in request.POST:
            Ninja.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],dojo=Dojo.objects.get(id=request.POST['dojo_select']))
    return redirect("/")

def delete(request):
    Dojo.objects.get(id=request.POST["dojo_data"]).delete()
    return redirect("/")
    