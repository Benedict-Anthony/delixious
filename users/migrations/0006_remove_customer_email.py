# Generated by Django 4.0.6 on 2022-08-02 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_rider_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
