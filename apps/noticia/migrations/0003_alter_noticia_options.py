# Generated by Django 4.0.6 on 2022-08-25 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ('-fecha',)},
        ),
    ]
