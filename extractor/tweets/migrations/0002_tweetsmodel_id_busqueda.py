# Generated by Django 2.2.4 on 2019-09-04 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetsmodel',
            name='id_busqueda',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
