# Generated by Django 4.2 on 2024-03-20 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last_name')),
                ('address', models.TextField(verbose_name='address')),
            ],
            options={
                'verbose_name': 'information',
                'verbose_name_plural': 'informations',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Title')),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='phons', to='contact.information', verbose_name='information')),
            ],
            options={
                'verbose_name': 'phone',
                'verbose_name_plural': 'phones',
            },
        ),
    ]
