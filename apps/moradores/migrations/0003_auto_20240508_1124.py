# Generated by Django 3.0 on 2024-05-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moradores', '0002_auto_20240508_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moradores',
            name='foto_morador',
            field=models.ImageField(upload_to='imagens/'),
        ),
    ]
