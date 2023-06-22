from django.forms import ModelForm
from .models import Inventory

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name' , 'cost_per_item' , 'quantiti_in_stock' , 'quantiti_sold']


class UpdateInvetoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name' , 'cost_per_item' , 'quantiti_in_stock' , 'quantiti_sold' , ]