# Generated by Django 3.2.16 on 2022-12-19 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
