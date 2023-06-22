from django.db import models



class Inventory(models.Model):
    name = models.CharField("Nombre Producto",max_length=100, null=False, blank=False)
    cost_per_item = models.DecimalField("Costo por item",max_digits=19, decimal_places=2, null=False, blank=False)
    quantiti_in_stock = models.IntegerField("Cantidad en stock",null=False,blank=False)
    quantiti_sold = models.IntegerField("Cantidad vendida",null=False,blank=False)
    sales= models.DecimalField("Ventas",max_digits=19, decimal_places=2, null=False, blank=False)
    stock_date = models.DateField("Fecha stock",auto_now_add=True)
    last_sales_date = models.DateField("fecha ultima venta",auto_now=True)
    
    
    def __str__(self):
        return self.name        