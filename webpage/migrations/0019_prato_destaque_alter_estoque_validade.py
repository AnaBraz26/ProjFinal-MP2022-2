# Generated by Django 4.1 on 2022-09-19 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webpage", "0018_alter_estoque_validade_alter_pedido_mesa"),
    ]

    operations = [
        migrations.AddField(
            model_name="prato",
            name="destaque",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="estoque",
            name="validade",
            field=models.DateField(
                default=datetime.datetime(2022, 9, 19, 0, 31, 58, 380240)
            ),
        ),
    ]
