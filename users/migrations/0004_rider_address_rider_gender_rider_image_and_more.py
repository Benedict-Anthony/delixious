# Generated by Django 4.0.6 on 2022-08-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_blog_review_rider'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rider',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=15),
        ),
        migrations.AddField(
            model_name='rider',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='rider',
            name='own_a_bike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rider',
            name='status',
            field=models.CharField(choices=[('married', 'married'), ('single', 'single')], default='single', max_length=15),
        ),
    ]
