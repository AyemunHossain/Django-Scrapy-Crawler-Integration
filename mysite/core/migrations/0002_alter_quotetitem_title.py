# Generated by Django 3.2.8 on 2022-01-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotetitem',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
