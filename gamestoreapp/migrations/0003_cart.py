# Generated by Django 5.1.1 on 2024-09-27 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestoreapp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalprice', models.FloatField(default=0.0)),
                ('cust_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestoreapp.customer')),
                ('product_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestoreapp.product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
