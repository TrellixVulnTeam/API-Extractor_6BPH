# Generated by Django 2.2.4 on 2019-09-25 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusquedaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('id_busqueda', models.IntegerField()),
                ('nombre', models.CharField(max_length=250)),
                ('ands', models.CharField(blank=True, max_length=250)),
                ('phrase', models.CharField(blank=True, max_length=250)),
                ('ors', models.CharField(blank=True, max_length=250)),
                ('nots', models.CharField(blank=True, max_length=250)),
                ('tags', models.CharField(blank=True, max_length=250)),
                ('respondiendo', models.CharField(blank=True, max_length=250)),
                ('mencionando', models.CharField(blank=True, max_length=250)),
                ('From', models.CharField(blank=True, max_length=250)),
                ('fecha_desde', models.DateField(blank=True, null=True)),
                ('fecha_hasta', models.DateField(blank=True, null=True)),
                ('fecha_peticion', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('es_cuenta', models.BooleanField(null=True)),
                ('tiene_tweets', models.BooleanField(null=True)),
            ],
        ),
    ]
