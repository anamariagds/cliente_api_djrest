# Generated by Django 3.0.8 on 2023-07-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]