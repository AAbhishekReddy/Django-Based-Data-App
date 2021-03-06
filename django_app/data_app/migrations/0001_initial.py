# Generated by Django 3.1.1 on 2020-10-01 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='new_york',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_symbol', models.CharField(max_length=100)),
                ('open_val', models.IntegerField()),
                ('high_val', models.IntegerField()),
                ('low_val', models.IntegerField()),
                ('close_prediction', models.IntegerField(default=0)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='beer_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_name', models.CharField(max_length=100)),
                ('review_aroma', models.IntegerField()),
                ('review_pallete', models.IntegerField()),
                ('review_taste', models.IntegerField()),
                ('review_appearance', models.IntegerField()),
                ('beer_abv', models.IntegerField()),
                ('prediction_review', models.IntegerField()),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
