# Generated by Django 4.0.4 on 2022-11-29 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_sale_commission_max_alter_sale_commission_min'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleproduct',
            options={'ordering': ['-created_at']},
        ),
    ]
