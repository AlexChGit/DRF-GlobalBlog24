# Generated by Django 3.1.7 on 2021-03-14 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('description', models.TextField(default='Description')),
                ('keywords', models.CharField(default='Key words', max_length=120)),
                ('creation_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('change_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('visible', models.BooleanField()),
                ('user', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-title', '-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('creation_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('change_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('visible', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post')),
            ],
            options={
                'ordering': ('-name', '-creation_date'),
            },
        ),
    ]
