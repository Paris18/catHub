# Generated by Django 2.2.1 on 2019-12-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_catelogue', '0003_auto_20191226_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='model',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='products',
            name='serial_no',
            field=models.CharField(max_length=256),
        ),
    ]
