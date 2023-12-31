# Generated by Django 4.2.2 on 2023-07-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('medical_aid', models.CharField(max_length=100)),
                ('medical_aid_number', models.CharField(max_length=100)),
                ('ice_contact', models.CharField(max_length=100)),
                ('ice_name', models.CharField(max_length=100)),
            ],
        ),
    ]
