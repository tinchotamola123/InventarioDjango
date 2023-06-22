from django.shortcuts import render , get_object_or_404 ,redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm , UpdateInvetoryForm

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    
    context = {
        "title" : "Lista de Inventario",
        "inventories" : inventories,
    }
    return render(request, "inventory/inventory_list.html", context=context)

@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        "inventory" : inventory
    }
    return render(request, "inventory/per_product.html", context=context)

@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantiti_sold'])
            new_inventory.save()
            return redirect("/inventory/")
    else:
        add_form = AddInventoryForm()
    
    return render(request, "inventory/inventory_add.html", {"form": add_form})

@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect("/inventory/")


@login_required
def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = UpdateInvetoryForm(data=request.POST)
        if updateForm.is_valid():
            inventory.name = updateForm.data['name']
            inventory.quantiti_in_stock = updateForm.data['quantiti_in_stock']
            inventory.quantiti_sold = updateForm.data['quantiti_sold']
            inventory.cost_per_item = updateForm.data['cost_per_item']
            inventory.sales = float(inventory.cost_per_item) * float(inventory.quantiti_sold)
            inventory.save()
            return redirect(f"/inventory/per_product/{pk}")
    else:
        updateForm = UpdateInvetoryForm(instance=inventory)
        
    context = {
        "form" : updateForm
    }
    return render(request, "inventory/inventory_update.html", context=context)