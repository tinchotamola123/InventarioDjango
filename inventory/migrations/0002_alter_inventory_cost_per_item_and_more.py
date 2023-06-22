# Generated by Django 4.2.2 on 2023-06-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory",
            name="cost_per_item",
            field=models.DecimalField(
                decimal_places=2, max_digits=19, verbose_name="Costo por item"
            ),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="last_sales_date",
            field=models.DateField(auto_now=True, verbose_name="fecha ultima venta"),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Nombre Producto"),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="quantiti_in_stock",
            field=models.IntegerField(verbose_name="Cantidad en stock"),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="quantiti_sold",
            field=models.IntegerField(verbose_name="Cantidad vendida"),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="sales",
            field=models.DecimalField(
                decimal_places=2, max_digits=19, verbose_name="Ventas"
            ),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="stock_date",
            field=models.DateField(auto_now_add=True, verbose_name="Fecha stock"),
        ),
    ]
