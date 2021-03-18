# Generated by Django 3.1.7 on 2021-03-18 09:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210313_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(blank=True, db_index=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, db_index=True, max_length=120),
        ),
    ]
