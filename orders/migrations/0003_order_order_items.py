# Generated by Django 3.2.16 on 2022-12-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_genre'),
        ('orders', '0002_auto_20221219_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
