# Generated by Django 2.2.10 on 2020-04-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0024_merge_20200413_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, max_length=765, null=True, verbose_name='Description/Notes'),
        ),
    ]
