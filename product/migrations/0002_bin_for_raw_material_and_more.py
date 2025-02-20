# Generated by Django 4.2.5 on 2025-02-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bin_for_raw_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='sales_return_voucher_master',
            name='narration',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sales_voucher_master_outward_scan',
            name='narration',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item_creation',
            name='bin',
            field=models.ManyToManyField(to='product.bin_for_raw_material'),
        ),
    ]
