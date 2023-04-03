# Generated by Django 4.1.7 on 2023-04-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('estado', models.TextField(default='por hacer', max_length=100)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
                ('modificado_el', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
