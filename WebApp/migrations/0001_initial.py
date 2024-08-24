# Generated by Django 5.0.6 on 2024-06-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_mail', models.EmailField(blank=True, max_length=10, null=True)),
                ('contact_sub', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_msg', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]