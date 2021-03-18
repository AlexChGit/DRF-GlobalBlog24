# Generated by Django 3.1.7 on 2021-03-18 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, default='Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, default='Key words', max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]