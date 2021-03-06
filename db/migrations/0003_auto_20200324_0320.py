# Generated by Django 2.2.8 on 2020-03-24 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_highlights_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlights',
            name='fotos',
            field=models.FileField(default=None, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='highlights',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=5, null=True),
        ),
    ]
