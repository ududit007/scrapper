# Generated by Django 2.2.2 on 2019-07-03 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0009_auto_20190702_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrappeddata',
            old_name='link',
            new_name='link_product',
        ),
    ]
