# Generated by Django 3.0 on 2024-03-19 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='porteiro',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='usuarios.Usuario', verbose_name='Usuário'),
        ),
    ]
