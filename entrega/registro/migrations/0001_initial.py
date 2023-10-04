# Generated by Django 4.2.5 on 2023-10-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(max_length=40)),
                ('codigo', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('fecha', models.DateField()),
                ('observaciones', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Escribano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.IntegerField()),
                ('tipo', models.CharField(max_length=40)),
            ],
        ),
    ]
