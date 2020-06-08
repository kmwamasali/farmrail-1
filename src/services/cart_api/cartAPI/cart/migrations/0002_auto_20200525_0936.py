# Generated by Django 3.0.6 on 2020-05-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='cart',
            name='Customer_email',
            field=models.CharField(default='name@example.com', max_length=75, unique=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='Customer_first_name',
            field=models.CharField(default='first name', max_length=50),
        ),
        migrations.AddField(
            model_name='cart',
            name='Customer_last_name',
            field=models.CharField(default='last name', max_length=50),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
