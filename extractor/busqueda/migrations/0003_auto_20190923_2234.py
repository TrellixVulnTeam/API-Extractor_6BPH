# Generated by Django 2.2.4 on 2019-09-23 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0002_auto_20190921_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busquedamodel',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='busquedamodel',
            name='tiene_tweets',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]