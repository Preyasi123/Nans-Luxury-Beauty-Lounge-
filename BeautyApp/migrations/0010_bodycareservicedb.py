# Generated by Django 5.0.6 on 2024-06-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeautyApp', '0009_makeupservicedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodycareservicedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bodycarecat_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Bodycare_category', models.CharField(blank=True, max_length=100, null=True)),
                ('Bodycare_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Bodycare_price', models.CharField(blank=True, max_length=100, null=True)),
                ('Bodycare_desc', models.CharField(blank=True, max_length=100, null=True)),
                ('Bodycare_image', models.ImageField(blank=True, null=True, upload_to='BodyCare Images')),
            ],
        ),
    ]
