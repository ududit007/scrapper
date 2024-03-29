# Generated by Django 2.2.2 on 2019-06-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0002_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrappedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('actual_price', models.FloatField(default=0)),
                ('saling_price', models.FloatField(default=0)),
                ('rating', models.FloatField(default=1)),
                ('image', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Scrapped_data',
                'verbose_name_plural': 'Scrapped_data',
                'db_table': 'scrapped_data',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
