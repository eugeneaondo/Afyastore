# Generated by Django 4.2.5 on 2023-10-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmode',
            name='mode',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
