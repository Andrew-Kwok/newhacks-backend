# Generated by Django 4.2.7 on 2023-11-05 06:14

from django.db import migrations, models
import django.db.models.deletion
import venue.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=venue.models.upload_path)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('zip_code', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('web', models.URLField(blank=True)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('category', models.CharField(choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('hybrid', 'Hybrid')], max_length=10)),
                ('suitable_for', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('parking', models.IntegerField()),
                ('traffic', models.FloatField()),
                ('scenery', models.FloatField()),
                ('comment', models.TextField(blank=True)),
                ('weather', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Venues',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VenueSurvey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField()),
                ('traffic', models.FloatField()),
                ('scenery', models.FloatField()),
                ('comment', models.TextField(blank=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.venue')),
            ],
            options={
                'verbose_name_plural': 'Venue Ratings',
                'ordering': ['venue'],
            },
        ),
    ]
