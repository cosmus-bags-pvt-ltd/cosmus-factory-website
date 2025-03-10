# Generated by Django 4.2.5 on 2025-03-03 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_deliverychallanmaster_balance_qty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverychallanproducts',
            name='balance_qty',
        ),
        migrations.RemoveField(
            model_name='sales_voucher_master_finish_goods',
            name='selected_godown',
        ),
        migrations.AddField(
            model_name='deliverychallanmaster',
            name='selected_godown',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.godown_finished_goods'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_delivery_challan_quantity_through_table',
            name='godown_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.godown_finished_goods'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sales_voucher_finish_goods',
            name='challan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.deliverychallanproducts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesvoucherdeliverychallan',
            name='balance_qty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salesvoucherdeliverychallan',
            name='total_qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
