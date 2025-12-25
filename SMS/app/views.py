from django.shortcuts import render, redirect
from .models import Flavor
from  .forms import FlavorForm

def flavor_list(request):
    flavors = Flavor.objects.all()
    return render(request, "flavor_list.html", {"flavors": flavors})

def update_flavor(request, id):
    flavor = Flavor.objects.get(id=id)

    if request.method == "POST":
        form = FlavorForm(request.POST, instance=flavor)
        if form.is_valid():
            form.save()
            return redirect("app:flavor_list")
    else:
        form = FlavorForm(instance=flavor)

    return render(request, "form.html", {"form": form})

def delete_flavor(request, id):
    flavor = Flavor.objects.get(id=id)

    if request.method == "POST":
        flavor.delete()
        return redirect("app:flavor_list")

    return render(request, "confirm_delete.html", {"flavor": flavor})

