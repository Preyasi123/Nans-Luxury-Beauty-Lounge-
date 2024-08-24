# Generated by Django 5.0.6 on 2024-06-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catg_desc', models.CharField(blank=True, max_length=100, null=True)),
                ('catg_name', models.ImageField(blank=True, null=True, upload_to='Category Images')),
            ],
        ),
    ]