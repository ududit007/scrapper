# Generated by Django 2.2.2 on 2019-06-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0006_auto_20190628_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrappeddata',
            name='keyword',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]