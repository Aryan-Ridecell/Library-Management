# Generated by Django 3.2.16 on 2022-12-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
