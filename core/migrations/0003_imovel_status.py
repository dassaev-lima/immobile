# Generated by Django 3.2.4 on 2021-06-29 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_venda_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='status',
            field=models.CharField(default='à venda', max_length=255),
        ),
    ]