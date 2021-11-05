from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from onzeapp.forms import CarForm
from onzeapp.models import Car


def index(request):
    cars = Car.objects.all()
    return TemplateResponse(request, "index.html", {"cars": cars})


def create_car(request):
    if request.method == 'GET':
        form = CarForm()
        return TemplateResponse(request, "create_car.html", {'form': form})
    elif request.method == 'POST':
        print(dict(request.POST))
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Inserted OK")
            return redirect("index")
        else:
            messages.error(request, "Something went wrong")
            return TemplateResponse(request, "create_car.html", {'form': form})


def delete_car(request):
    if request.method == 'POST':
        for key in list(request.POST.keys())[:-1]:
            Car.objects.filter(id=key).delete()
    messages.info(request, "Item deleted")
    return redirect("index")
