# Generated by Django 2.2.2 on 2019-06-27 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0003_auto_20190627_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrappeddata',
            old_name='saling_price',
            new_name='selling_price',
        ),
    ]
