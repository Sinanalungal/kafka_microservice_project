# Generated by Django 5.0.3 on 2024-04-02 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderedproducts',
            old_name='product',
            new_name='orderdetails',
        ),
        migrations.RemoveField(
            model_name='orderedproducts',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orderedproducts',
            name='country',
        ),
        migrations.RemoveField(
            model_name='orderedproducts',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='orderedproducts',
            name='house',
        ),
        migrations.RemoveField(
            model_name='orderedproducts',
            name='street',
        ),
        migrations.RemoveField(
            model_name='orderedproducts',
            name='zipcode',
        ),
    ]
