# Generated by Django 2.1.7 on 2019-03-23 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangomen', '0006_auto_20190323_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state', to='djangomen.Order_State'),
        ),
    ]
