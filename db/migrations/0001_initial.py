# Generated by Django 2.2.8 on 2020-03-24 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id_highlight', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=3, max_digits=5)),
                ('fotos', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id_tipos', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id_lugar', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('zona', models.CharField(choices=[('ZS', 'Zona Sur'), ('ZC', 'Zona Centro'), ('ZM', 'Zona Miraflores'), ('ZO', 'Zona Obrajes ')], default='ZA', max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('tel', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('fb', models.CharField(max_length=100)),
                ('insta', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
                ('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Highlights')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Tipos')),
            ],
        ),
    ]