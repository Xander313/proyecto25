# Generated by Django 5.2.1 on 2025-05-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0002_reserva_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateTimeField(),
        ),
    ]
